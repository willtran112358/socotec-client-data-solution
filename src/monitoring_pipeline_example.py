"""
SOCOTEC Vietnam monitoring data pipeline — reference for VN intern JD workflow.

Operational tasks from public job posts (2025-2026):
  - Equipment health checks
  - Raw sensor data processing
  - Anomaly detection for potential issues
  - Periodic reports (daily, weekly, monthly)
  - Project-scoped data quality
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    avg,
    col,
    count,
    current_timestamp,
    lit,
    max as spark_max,
    min as spark_min,
    stddev,
    sum as spark_sum,
    when,
)


def build_sensor_health_kpi(spark: SparkSession):
    """Flag offline sensors — blocks report sign-off when equipment is unhealthy."""
    health = spark.table("silver_sensor_health")
    sensors = spark.table("silver_sensors")

    return (
        health.join(sensors, "sensor_id", "inner")
        .groupBy("project_id", "sensor_id", "sensor_type")
        .agg(
            spark_max("event_ts").alias("last_seen_at"),
            spark_max("battery_pct").alias("latest_battery_pct"),
        )
        .withColumn(
            "health_status",
            when(
                col("last_seen_at") < current_timestamp() - lit("2 hours").cast("interval"),
                lit("OFFLINE"),
            )
            .when(col("latest_battery_pct") < 15, lit("LOW_BATTERY"))
            .otherwise(lit("HEALTHY")),
        )
    )


def build_anomaly_kpi(spark: SparkSession):
    """Detect threshold breaches and statistical outliers on validated readings."""
    readings = spark.table("silver_sensor_readings")
    config = spark.table("silver_sensor_config")

    joined = readings.join(config, ["sensor_id", "config_version"], "inner")

    stats = joined.groupBy("project_id", "sensor_id", "sensor_type").agg(
        avg("value").alias("avg_value"),
        stddev("value").alias("stddev_value"),
        count("reading_id").alias("reading_count"),
    )

    flagged = (
        joined.join(stats, ["project_id", "sensor_id", "sensor_type"], "inner")
        .withColumn(
            "anomaly_type",
            when(
                (col("value") < col("threshold_min")) | (col("value") > col("threshold_max")),
                lit("THRESHOLD_BREACH"),
            )
            .when(
                col("stddev_value").isNotNull()
                & (col("value") > col("avg_value") + lit(3) * col("stddev_value")),
                lit("STATISTICAL_OUTLIER"),
            )
            .otherwise(lit(None)),
        )
        .filter(col("anomaly_type").isNotNull())
    )

    return flagged.groupBy("project_id", "sensor_id", "anomaly_type").agg(
        count("reading_id").alias("anomaly_count"),
        spark_max("reading_ts").alias("last_anomaly_at"),
    )


def build_periodic_report(spark: SparkSession, report_period: str):
    """Aggregate monitoring KPIs for daily / weekly / monthly client reports."""
    anomalies = spark.table("gold_sensor_anomaly_kpi")
    health = build_sensor_health_kpi(spark)

    offline = health.filter(col("health_status") == "OFFLINE")

    return (
        anomalies.crossJoin(spark.range(1).select(lit(report_period).alias("report_period")))
        .groupBy("project_id", "report_period")
        .agg(
            spark_sum("anomaly_count").alias("total_anomalies"),
            count("sensor_id").alias("sensors_with_anomalies"),
        )
        .join(
            offline.groupBy("project_id").agg(count("sensor_id").alias("offline_sensor_count")),
            "project_id",
            "left",
        )
        .fillna({"offline_sensor_count": 0})
        .withColumn("published_at", current_timestamp())
    )


def run():
    spark = SparkSession.builder.appName("socotec-monitoring-pipeline").getOrCreate()

    health_kpi = build_sensor_health_kpi(spark)
    health_kpi.write.mode("overwrite").format("delta").saveAsTable("gold_sensor_health_kpi")

    anomaly_kpi = build_anomaly_kpi(spark)
    anomaly_kpi.write.mode("overwrite").format("delta").saveAsTable("gold_sensor_anomaly_kpi")

    for period in ("daily", "weekly", "monthly"):
        report = build_periodic_report(spark, period)
        report.write.mode("overwrite").format("delta").saveAsTable(
            f"gold_monitoring_report_{period}"
        )


if __name__ == "__main__":
    run()
