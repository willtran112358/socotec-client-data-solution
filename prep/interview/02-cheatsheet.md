# Cheatsheet — SOCOTEC Lead DE technical interview

One-page reference. Pair with [`01-technical-qa.md`](01-technical-qa.md) for full answers.

---

## SOCOTEC stack (from JD / public profiles)

| Layer | Tech |
|-------|------|
| Cloud | AWS (S3, IAM, likely MWAA or self-hosted Airflow) |
| Lakehouse | Databricks + Delta Lake |
| Ingestion | Fivetran / Airbyte, CDC, Kafka |
| Processing | PySpark batch + Structured Streaming |
| Orchestration | Airflow |
| BI / SQL | Power BI, Databricks SQL |
| Governance | OpenMetadata-style catalog, DQ, Unity Catalog |
| DevOps | Git/GitLab, CI/CD, notebooks |

---

## TIC business — 15-second context

Testing, Inspection, Certification for construction / infrastructure / environment. Data opportunity: turn inspection + compliance data into **client analytics products** (risk KPIs, compliance APIs, ESG, predictive maintenance). SOCOTEC runs a global **Data & AI Hub** and an international Lakehouse modernization.

---

## Medallion layers

```
Sources → Bronze (raw Delta) → Silver (conformed, PII-safe) → Gold (KPIs, APIs) → BI / API / GenAI
```

| Layer | Write pattern | Quality |
|-------|---------------|---------|
| Bronze | Append | Minimal — schema drift OK |
| Silver | Merge / DLT stream | Expectations, typing, dedup |
| Gold | Merge upsert | Contract + SQL DQ + SLA |

---

## PySpark — aggregates and filters (interview pattern)

```python
from pyspark.sql.functions import col, count, avg, sum, max, min, countDistinct
from pyspark.sql.functions import current_date, date_sub, when, lit

# Filter
df.filter((col("status") != "CANCELLED") & col("score").isNotNull())

# Multiple conditions
df.filter(col("criticality_level").isin("HIGH", "CRITICAL"))

# Date window
df.filter(col("inspection_date") >= date_sub(current_date(), 90))

# Join (prefer filter-before-join)
df.join(other, on="asset_id", how="inner")

# Aggregate
df.groupBy("client_id", "asset_id").agg(
    count("inspection_id").alias("inspection_count"),
    avg("non_conformity_score").alias("avg_score"),
    max("inspection_date").alias("last_inspection"),
)

# Post-agg filter
. filter(col("inspection_count") >= 2)

# Conditional column
.withColumn("risk_band", when(col("avg_score") >= 70, "HIGH").otherwise("LOW"))

# Order
.orderBy(col("avg_score").desc())
```

**Imports to remember:** `col`, `count`, `avg`, `countDistinct`, `sum`, `max`, `min`, `when`, `lit`, `current_date`, `date_sub`, `sha2`, `concat_ws`, `current_timestamp`.

---

## PySpark — window functions (common follow-up)

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank, lag

w = Window.partitionBy("client_id").orderBy(col("inspection_date").desc())

df.withColumn("rn", row_number().over(w)).filter(col("rn") == 1)  # latest per client
```

---

## Delta Lake essentials

```python
# Read / write
df.write.format("delta").mode("append").save(path)
spark.read.format("delta").load(path)

# MERGE (upsert)
from delta.tables import DeltaTable
DeltaTable.forPath(spark, path).alias("t").merge(
    source.alias("s"), "t.client_id = s.client_id AND t.asset_id = s.asset_id"
).whenMatchedUpdateAll().whenNotMatchedInsertAll().execute()

# Time travel
spark.read.format("delta").option("versionAsOf", 5).load(path)

# Optimize
spark.sql("OPTIMIZE delta.`path` ZORDER BY (client_id, asset_id)")
```

---

## DLT expectations (repo pattern)

```python
@dlt.table(name="silver_inspections")
@dlt.expect_or_drop("valid_asset_id", "asset_id IS NOT NULL")
@dlt.expect_or_drop("valid_inspection_date", "inspection_date IS NOT NULL")
def silver_inspections():
    return spark.readStream.table("bronze_inspections").transform(...)
```

| Decorator | On failure |
|-----------|------------|
| `@dlt.expect` | Metric only |
| `@dlt.expect_or_drop` | Drop row |
| `@dlt.expect_or_fail` | Fail pipeline |

---

## Gold DQ SQL (repo pattern)

```sql
-- Freshness
SELECT CASE WHEN MAX(updated_at) >= current_timestamp() - INTERVAL 1 DAY
       THEN 'PASS' ELSE 'FAIL' END FROM gold_asset_risk_kpi;

-- Null keys
SELECT COUNT(*) FROM gold_asset_risk_kpi
WHERE client_id IS NULL OR asset_id IS NULL;

-- Range
SELECT COUNT(*) FROM gold_asset_risk_kpi
WHERE avg_non_conformity_score < 0 OR avg_non_conformity_score > 100;
```

---

## Join cheat sheet

| Type | Result |
|------|--------|
| `inner` | Matched rows only |
| `left` | All left + matched right |
| `left_anti` | Left rows with no match on right |
| `cross` | Cartesian (avoid) |

---

## Data contract fields (repo)

`product_name`, `version`, `owner_team`, `sla.refresh_frequency`, `sla.availability`, `fields[]`, `security.contains_pii`, `security.access_policy`

---

## Repo file → interview mapping

| File | Talking point |
|------|---------------|
| `current_pipeline.py` | POC ETL — overwrite, no DQ, no PII |
| `proposed_dlt_pipeline.py` | Silver expectations + Gold agg |
| `proposed_data_quality_checks.sql` | Post-publish validation |
| `api_contract_example.json` | Client-facing product spec |
| `interview_pyspark_example.py` | Live coding reference |

---

## `current_pipeline.py` critique (30 sec)

1. Overwrite → use MERGE for Gold  
2. No DQ gates  
3. Left join without orphan policy  
4. No PII handling  
5. Hard-coded paths → Unity Catalog / config  

---

## Lead DE phrases (use naturally)

- *"I'd filter before the join to cut shuffle."*
- *"For client-facing Gold, I'd enforce the contract in CI."*
- *"Bronze is immutable; corrections happen in Silver upward."*
- *"I'd MERGE on `(client_id, asset_id)` for idempotent daily refresh."*
- *"DQ CRITICAL blocks publish; MEDIUM opens a ticket."*

---

## Spark performance — top 5

1. Filter early, select only needed columns  
2. Avoid `collect()` on large datasets  
3. Partition by date / `client_id`  
4. Broadcast small dimension tables (`broadcast(df)`)  
5. Enable AQE on Databricks (default on recent DBR)  

---

## Entity model (quick)

```
CUSTOMER → PROJECT → SITE → ASSET ← INSPECTION → FINDING → WORK_ORDER
                              ↓
                      COMPLIANCE_RESULT ← REGULATION_RULE
```

Gold marts: `gold_asset_risk_kpi`, `gold_compliance_kpi`, `gold_maintenance_sla_kpi`.

---

## 30-min pre-interview checklist

- [ ] Write `interview_pyspark_example.py` from memory  
- [ ] Explain Bronze / Silver / Gold with one SOCOTEC example each  
- [ ] Recite 3 DQ checks on Gold  
- [ ] Critique `current_pipeline.py` (5 bullets)  
- [ ] Prepare 2 questions for Lead DE  
