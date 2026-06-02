"""
SOCOTEC interview live-coding reference — PySpark aggregates and filters.

Reported interview prompt (Glassdoor, Dec 2025): "Write a PySpark query with
aggregates and filters."

Domain: inspection and asset data aligned with this repo's data model.
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, col, count, current_date, date_sub


def top_risk_assets_by_client():
    spark = SparkSession.builder.appName("socotec-interview-pyspark").getOrCreate()

    inspections = spark.table("silver_inspections")
    assets = spark.table("silver_assets")

    # Filter: active inspections in last 90 days, exclude cancelled
    recent = inspections.filter(
        (col("inspection_status") != "CANCELLED")
        & (col("inspection_date") >= date_sub(current_date(), 90))
    )

    # Join + aggregate: avg non-conformity score and inspection count per client/asset
    kpi = (
        recent.join(assets, on="asset_id", how="inner")
        .filter(col("criticality_level").isin("HIGH", "CRITICAL"))
        .groupBy("client_id", "asset_id", "criticality_level")
        .agg(
            count("inspection_id").alias("inspection_count"),
            avg("non_conformity_score").alias("avg_non_conformity_score"),
        )
        .filter(col("inspection_count") >= 2)
        .orderBy(col("avg_non_conformity_score").desc())
    )

    return kpi


if __name__ == "__main__":
    top_risk_assets_by_client().show(20, truncate=False)
