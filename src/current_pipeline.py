from pyspark.sql import SparkSession
from pyspark.sql.functions import col, current_timestamp


def run():
    spark = SparkSession.builder.appName("socotec-current-pipeline").getOrCreate()

    inspections = spark.read.format("parquet").load("s3://socotec-raw/inspections/")
    assets = spark.read.format("parquet").load("s3://socotec-raw/assets/")

    joined = (
        inspections.join(assets, on="asset_id", how="left")
        .filter(col("inspection_status") != "CANCELLED")
        .withColumn("processed_at", current_timestamp())
    )

    (
        joined.write.mode("overwrite")
        .format("delta")
        .save("s3://socotec-curated/inspection_asset_snapshot/")
    )


if __name__ == "__main__":
    run()
