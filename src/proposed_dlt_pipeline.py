import dlt
from pyspark.sql.functions import col, current_timestamp, sha2, concat_ws


@dlt.table(
    name="silver_inspections",
    comment="Validated and pseudonymized inspections.",
    table_properties={"quality": "silver"},
)
@dlt.expect_or_drop("valid_asset_id", "asset_id IS NOT NULL")
@dlt.expect_or_drop("valid_inspection_date", "inspection_date IS NOT NULL")
def silver_inspections():
    raw = spark.readStream.table("bronze_inspections")
    return (
        raw.withColumn(
            "inspector_key",
            sha2(concat_ws("||", col("inspector_email"), col("country_code")), 256),
        )
        .drop("inspector_email")
        .withColumn("updated_at", current_timestamp())
    )


@dlt.table(
    name="gold_asset_risk_kpi",
    comment="Client-facing KPI table for risk and compliance analytics.",
    table_properties={"quality": "gold"},
)
def gold_asset_risk_kpi():
    inspections = dlt.read("silver_inspections")
    assets = spark.table("silver_assets")
    return (
        inspections.join(assets, "asset_id", "inner")
        .groupBy("client_id", "asset_id", "criticality_level")
        .agg(
            {"inspection_id": "count", "non_conformity_score": "avg"},
        )
        .withColumnRenamed("count(inspection_id)", "inspection_count")
        .withColumnRenamed("avg(non_conformity_score)", "avg_non_conformity_score")
    )
