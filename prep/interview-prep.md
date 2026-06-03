# SOCOTEC DE technical interview — Lead DE round

> **Audience:** Lead Data Engineer interviewer at SOCOTEC Data & AI Hub (Massy, Ile-de-France).  
> **Case study repo:** [`../README.md`](../README.md) · Code samples: [`../src/`](../src/)  
> **Reported topic (Glassdoor, Dec 2025):** PySpark query with aggregates and filters.

**Contents**

| Section | What's inside |
|---------|---------------|
| [1. Strategy](#1-strategy) | Signals, opening pitch, repo walkthrough, interview flow, 30-min drill |
| [1.6 Perrine Q&A](#16-perrine-tcheeko-lead-de--estimate-qa) | Likely Lead DE questions (main interviewer) |
| [1.7 Viet Q&A](#17-vu-tran-viet-em-platform-vn--estimate-qa) | Secondary VN site questions (1–2) |
| [1.8 Business & products](#18-socotec-business-products--what-they-care-about) | Company, services, Green Trust, VN monitoring, role demands |
| [2. Cheatsheet](#2-cheatsheet) | Stack, syntax, patterns — skim before the call |
| [3. Technical Q&A](#3-technical-qa) | Mindmaps 10 min + full model answers (PySpark, DLT, DQ, **business Q15–Q25**) |
| [4. Questions to ask](#4-questions-to-ask-the-lead-de) | Pick 2–3 for the end |

Live-coding code file: [`src/interview_pyspark_example.py`](../src/interview_pyspark_example.py)

---

## 1. Strategy

### 1.1 Signals the Lead DE looks for

| Signal | How to demonstrate |
|--------|-------------------|
| **PySpark fluency** | Write clean aggregates + filters on inspection/asset data without IDE autocomplete |
| **Production mindset** | Mention DQ gates, idempotency, backfill, SLA, cost — not just "make it work" |
| **Lakehouse literacy** | Bronze/Silver/Gold, Delta, DLT expectations, merge vs overwrite trade-offs |
| **Governance awareness** | PII pseudonymization, data contracts, client-scoped RBAC |
| **Business framing** | Tie answers to TIC value chain: inspections → compliance → client risk KPIs |
| **Senior judgment** | Trade-offs, when to stop perfecting, how you'd mentor a mid-level DE |

**Core message:** You understand SOCOTEC's stack (AWS + Databricks + Delta + Airflow) and can move their inspection/compliance data from raw landing to governed client-facing products.

### 1.2 Opening pitch (60 seconds)

> I'm a data engineer focused on lakehouse platforms — Spark, Delta Lake, and medallion pipelines on AWS. I've studied SOCOTEC's TIC business and Data & AI Hub direction: turning field inspection and compliance data into recurring analytics products — asset risk KPIs, compliance dashboards, client APIs.  
>  
> This repo is my working blueprint: a current-style Spark ETL, a proposed DLT pipeline with quality expectations, Gold-layer SQL checks, and an API contract example. I'm ready to go deep on PySpark, pipeline design, and how we'd harden this for production at SOCOTEC scale.

### 1.3 How to use this repo in the interview

| If they ask… | Point to… |
|--------------|-----------|
| "Walk me through your understanding of our data platform" | README §2 Architecture + §1 Business |
| "What's wrong with a simple ETL?" | `src/current_pipeline.py` — no DQ, left join fan-out risk, overwrite mode, no PII handling |
| "How would you improve it?" | `src/proposed_dlt_pipeline.py` — expectations, pseudonymization, Gold aggregation |
| "How do you validate Gold tables?" | `src/proposed_data_quality_checks.sql` |
| "How do external clients consume data?" | `src/api_contract_example.json` |
| Live PySpark coding | `src/interview_pyspark_example.py` + [Cheatsheet § PySpark](#pyspark--aggregates-and-filters-interview-pattern) |

### 1.4 Likely interview flow

```mermaid
flowchart LR
    A["Intro and background"] --> B["Stack and architecture discussion"]
    B --> C["Live PySpark: aggregates and filters"]
    C --> D["Design or code review of a pipeline"]
    D --> E["Governance, DQ, or Delta deep dive"]
    E --> F["Your questions"]

    classDef step fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1
    class A,B,C,D,E,F step
```

**Time split (typical 45–60 min technical):** ~15 min discussion · ~20 min live coding · ~15 min design/review · ~5 min your questions.

### 1.5 Before the call — 30-minute drill

1. **Skim** [§2 Cheatsheet](#2-cheatsheet) once (10 min).
2. **Write from memory** the PySpark example in `src/interview_pyspark_example.py` on paper or a blank notebook (10 min).
3. **Explain aloud** why `current_pipeline.py` is insufficient and how DLT fixes it (5 min).
4. **Prepare 3 questions** for the Lead DE ([§4](#4-questions-to-ask-the-lead-de)).
5. **Skim** [§1.6 Perrine Q&A](#16-perrine-tcheeko-lead-de--estimate-qa), [§1.7 Viet Q&A](#17-vu-tran-viet-em-platform-vn--estimate-qa), and [§1.8 Business](#18-socotec-business-products--what-they-care-about) (5 min).

### 1.6 Perrine TCHEEKO (Lead DE) — estimate Q&A

**Role:** Team Leader Data Engineer @ SOCOTEC Data & AI Hub (GCP certified, PySpark/SQL, lakehouse, documentation & teamwork). **Main technical interviewer** — expect depth on Spark, Delta/DLT, and production habits.

| Question | Answer |
|----------|--------|
| Walk me through a PySpark query with aggregates and filters. | Read **Silver**; filter early (`CANCELLED`, 90-day window, criticality); **inner** join on `asset_id`; `groupBy` client/asset; `count` + `avg`; post-filter `inspection_count >= 2`; order by risk — see `interview_pyspark_example.py`. |
| When do you use a **left anti** join? | Rows in left with **no** match on right — e.g. assets with zero inspections in the period for a DQ report (she teaches this pattern on LinkedIn). |
| Why **CTEs** instead of nested subqueries? | Readability, reuse of logic blocks, easier review in PRs — same plan as subqueries in Spark SQL. |
| **union** vs **unionByName** in PySpark? | `union` needs same column count/order; **unionByName** aligns by name — safer when schemas drift between sources. |
| Bronze / Silver / Gold for SOCOTEC inspection data? | Bronze: raw append; Silver: conformed, deduped, **pseudonymized**; Gold: narrow KPIs (`gold_asset_risk_kpi`) for BI/API — never expose Bronze to clients. |
| **MERGE** vs **overwrite** on Gold? | Overwrite = POC rebuild; production Gold = **MERGE** on `(client_id, asset_id)` + `updated_at` for idempotent daily refresh. |
| DLT `@dlt.expect` vs `@dlt.expect_or_drop`? | `expect` = metric only; **expect_or_drop** = drop bad rows in Silver (null `asset_id`, `inspection_date`) — repo `proposed_dlt_pipeline.py`. |
| How do you explore a huge table without blowing cost? | Sample first (`TABLESAMPLE` / limited partitions / `limit` after filter), select only needed columns, avoid full scans in dev — then validate on representative slice. |
| How do you handle **PII / GDPR** in pipelines? | Pseudonymize in Silver (`sha2` + drop raw email); document in catalog; Gold contract `contains_pii: false`; right-to-erasure process on keys. |
| Critique our POC ETL (`current_pipeline.py`). | No DQ, overwrite on curated path, left join without orphan policy, no PII, hard-coded paths — fix with DLT expectations + MERGE + Unity Catalog. |
| How much **documentation** do you write? | Update runbooks and contract fields each sprint — enough that the next DE or BA can operate without a tribal knowledge call (matches her team norm). |
| **Solo vs team** — preference? | Team — complex lakehouse needs code review, on-call pairs, and shared standards; I escalate early when prod data is at risk. |
| **Databricks / AWS** vs your GCP background? | Same lakehouse patterns (Spark, Delta, Airflow); I learn the cloud control plane per client — SOCOTEC JD is AWS + Databricks + Delta. |
| Why **SOCOTEC** and this DE role? | Global TIC + **Green Trust/BIM & Data** scale; Data Hub turns inspections and **monitoring streams** into products; lakehouse (AWS, Databricks, Delta); acquisitions need conformed Silver; role funds certs and works with international + VN monitoring teams. |
| What is **SOCOTEC** in one sentence? | Independent **TIC** group building trust for safer, sustainable assets — inspections, labs, certification, and increasingly **digital monitoring** and data products. |
| What would you do in the **first 90 days**? | Map sources and contracts; ship one vertical Bronze→Gold slice with DQ; align with Lead on CI gates and client API readiness. |

### 1.7 Vu Tran-Viet (EM Platform, VN site) — estimate Q&A

**Role:** Engineering Platform Manager @ SOCOTEC Monitoring Vietnam (instrumentation, BIM, monitoring, mechanical/aerospace background). **Secondary interviewer** — lighter on Spark; focus on collaboration, VN–global delivery, and explaining data value to engineering teams.

| Question | Answer |
|----------|--------|
| How will your data work **support monitoring / instrumentation** teams in Vietnam? | Reliable time-series and asset master data in Silver; Gold KPIs (freshness, anomaly flags) that monitoring dashboards and BIM workflows can trust — clear SLA and ownership with VN engineering. |
| How do you **explain a pipeline or data issue** to non-data engineers? | Business impact first (e.g. “dashboard stale 26h → field teams see old risk scores”), one diagram Bronze→Gold, one decision needed — no Spark jargon unless they ask. |
| What do you know about **SOCOTEC’s business**? | Global **TIC** leader (~15k staff, 250k clients, 26 countries); trusted third party across construction, infrastructure, industry; strategic push on **Green Trust** (monitoring, ESG) and **BIM & Data**; Data Hub productizes inspection/compliance/monitoring data — see [§1.8](#18-socotec-business-products--what-they-care-about). |
| Why **monitoring data** is different from inspection PDFs? | Higher frequency time-series, 24/7 SLA, anomaly detection; needs streaming/micro-batch Bronze + asset alignment in Silver; Gold freshness drives field response — Cementys VN model. |

---

### 1.8 SOCOTEC business, products & what they care about

> **Sources:** [socotec.com](https://www.socotec.com) corporate site, country pages (VN, FR, UAE), news (FREEDA AI, acquisitions), public sustainability reports. Estimates marked where not published.

#### 1.8.1 Elevator pitch — company (30 seconds)

SOCOTEC is a **global TIC group** (Testing, Inspection, Certification): a **trusted third party** for construction, infrastructure, and industry clients from project design through operation and decommissioning. ~15,000 people, 250,000 clients, 26 countries. Beyond classic site inspections, the group invests in **Green Trust** (environmental and structural monitoring), **BIM & Data**, and an international **Data & AI Hub** to turn operational data into recurring digital products — risk KPIs, compliance evidence, ESG and monitoring SaaS.

#### 1.8.2 Service lines → data products (map for DE answers)

| SOCOTEC service (public) | Field output | Lakehouse entity / Gold product |
|--------------------------|--------------|----------------------------------|
| Technical inspection & verification | Inspection reports, schedules | `silver_inspections` → `gold_asset_risk_kpi` |
| Environment & safety / water quality | Samples, thresholds, alerts | `gold_environmental_kpi`, streaming Bronze for sensors |
| Green Building / energy optimization | Audits, consumption trajectories | ESG marts, client carbon KPIs |
| Fire & life safety | Test certs, pass/fail | `gold_compliance_kpi` + evidence links |
| Certification (ISO, GHG) | Audit outcomes | Separate cert domain; less overlap with inspection repo |
| **BlueTrust / structural monitoring** | Time-series, 24/7 dashboards | High-frequency Bronze, anomaly Gold, SLA freshness |
| Training | Attendance, certs | Lower priority for client API hub |

#### 1.8.3 Strategic pillars (say these names in interview)

| Pillar | Meaning | Why Data Hub cares |
|--------|---------|-------------------|
| **Green Trust** | Safer, sustainable assets via monitoring & ESG | Sensor + environmental data at scale |
| **Trust & Tech** | Digital tools on top of physical expertise | SaaS, real-time platforms (VN Cementys) |
| **BIM & Data** | Model-linked project/asset data | Unified asset IDs across BIM, inspections, monitoring |
| **Industry 4.0 / Smart cities** | Connected infrastructure | IoT → Bronze, predictive maintenance Gold |

**Recent signal:** SOCOTEC × **FREEDA** (Jan 2026) — AI on architectural plans → expect interview interest in **governed Gold metrics** feeding ML, not raw Bronze in models.

#### 1.8.4 Vietnam & global monitoring (for Viet + Perrine)

**Cementys (SOCOTEC Vietnam)** — public scope:

- Structural health monitoring (transport, energy infrastructure)
- Environmental: noise, vibration, water, geotechnical, topography
- Proprietary visualisation + **integrated digital platform** (ML, ageing analysis, maintenance SaaS)

**Your bridge sentence:** *"Massy lakehouse standardizes client and asset master data; Vietnam streams monitoring into the same Silver/Gold contracts so global dashboards and VN 24/7 ops share one truth."*

#### 1.8.5 What the Lead DE / Data Hub likely demands (estimate)

| They care about | You show |
|-----------------|----------|
| Production-grade Spark | Live aggregates/filters; filter-before-join; explicit aliases |
| Medallion discipline | Bronze immutable; Silver pseudonymized; Gold narrow + MERGE |
| Trust & compliance | GDPR, contracts, `contains_pii: false`, RBAC by `client_id` |
| Product delivery | One vertical slice to API/Power BI with DQ gates |
| Cost & ops | Partition prune, job clusters, no full-table `collect()` in dev |
| Cross-site teamwork | Document contracts; align with VN monitoring SLAs |
| Business literacy | Tie pipeline choices to TIC + monitoring client value |

#### 1.8.6 Business Q&A — quick table (add to §E)

| Question | Short answer |
|----------|--------------|
| What does SOCOTEC do? | TIC + advisory as independent trusted third party; construction, infrastructure, industry, environment. |
| Who are the clients? | Contractors, asset owners, insurers, public authorities, utilities — 250k clients globally. |
| How does SOCOTEC make money? | Project fees, recurring inspections, monitoring contracts, certification audits, training; data products are **margin-accretive** add-on. |
| Name a digital product. | Asset risk KPI API, compliance automation, monitoring SaaS with real-time Gold feeds. |
| Acquisitions and data? | Labs, geodata, monitoring firms → more sources; need **Silver conformation** before client Gold. |
| UAE / mega-project example? | Third-party design review, H&S, MEP on Louvre Abu Dhabi, Sea World — **evidence-heavy** compliance trail. |
| Difference TIC vs Cementys monitoring? | TIC = episodic inspections/certificates; monitoring = **continuous** time-series + 24/7 SLA. |

#### 1.8.7 Opening pitch — business line (optional 15 sec add-on)

> I also looked at SOCOTEC’s **Green Trust** and **BIM & Data** direction — especially structural and environmental monitoring in Vietnam and the push to industrialize plan analysis with AI — so I’d design pipelines that serve both classic inspection KPIs and high-frequency monitoring with the same governed asset model.

#### 1.8.8 5-minute business drill (before call)

1. Say **TIC + trusted third party + 15k/250k/26** without notes.  
2. Name **3 service lines** and one **data product** each.  
3. Explain **Cementys** in one sentence and link to Silver/Gold.  
4. Answer: *"Why SOCOTEC Data Hub?"* — international lakehouse, productized compliance/risk data, GenAI on certified metrics.  
5. Skim README §1.4–1.10 for numbers and acquisitions context.

---

## 2. Cheatsheet

### SOCOTEC stack (from JD / public profiles)

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

### TIC business — 15-second context

**Testing, Inspection, Certification** — global leader, *trusted third party*, construction / infrastructure / industry / environment. **~15k employees · 250k clients · 26 countries.** Also: **Green Trust** (monitoring, ESG), **BIM & Data**, certification hubs in APAC. Data opportunity: inspection + compliance + **sensor monitoring** → **client products** (risk KPIs, APIs, ESG, predictive maintenance). **Data & AI Hub** (Massy) + international lakehouse on AWS/Databricks.

### SOCOTEC products & sectors (30-second)

| Bucket | Examples |
|--------|----------|
| **Services** | Green Building, TIV, Specialty Engineering, Fire, Environment & Safety, Certification, Training |
| **Sectors** | Construction, Real Estate, Infrastructure, Industry, Energy & Utilities |
| **Digital** | BlueTrust Monitoring, structural/optic monitoring, Cementys platform (VN), FREEDA AI plans |
| **Gold in repo** | `gold_asset_risk_kpi`, `gold_compliance_kpi`, `gold_maintenance_sla_kpi` |

### Medallion layers

```
Sources → Bronze (raw Delta) → Silver (conformed, PII-safe) → Gold (KPIs, APIs) → BI / API / GenAI
```

| Layer | Write pattern | Quality |
|-------|---------------|---------|
| Bronze | Append | Minimal — schema drift OK |
| Silver | Merge / DLT stream | Expectations, typing, dedup |
| Gold | Merge upsert | Contract + SQL DQ + SLA |

### PySpark — aggregates and filters (interview pattern)

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
.filter(col("inspection_count") >= 2)

# Conditional column
.withColumn("risk_band", when(col("avg_score") >= 70, "HIGH").otherwise("LOW"))

# Order
.orderBy(col("avg_score").desc())
```

**Imports to remember:** `col`, `count`, `avg`, `countDistinct`, `sum`, `max`, `min`, `when`, `lit`, `current_date`, `date_sub`, `sha2`, `concat_ws`, `current_timestamp`.

### PySpark — window functions (common follow-up)

```python
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank, lag

w = Window.partitionBy("client_id").orderBy(col("inspection_date").desc())

df.withColumn("rn", row_number().over(w)).filter(col("rn") == 1)  # latest per client
```

### Delta Lake essentials

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

### DLT expectations (repo pattern)

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

### Gold DQ SQL (repo pattern)

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

### Join cheat sheet

| Type | Result |
|------|--------|
| `inner` | Matched rows only |
| `left` | All left + matched right |
| `left_anti` | Left rows with no match on right |
| `cross` | Cartesian (avoid) |

### Data contract fields (repo)

`product_name`, `version`, `owner_team`, `sla.refresh_frequency`, `sla.availability`, `fields[]`, `security.contains_pii`, `security.access_policy`

### Repo file → interview mapping

| File | Talking point |
|------|---------------|
| `current_pipeline.py` | POC ETL — overwrite, no DQ, no PII |
| `proposed_dlt_pipeline.py` | Silver expectations + Gold agg |
| `proposed_data_quality_checks.sql` | Post-publish validation |
| `api_contract_example.json` | Client-facing product spec |
| `interview_pyspark_example.py` | Live coding reference |

### `current_pipeline.py` critique (30 sec)

1. Overwrite → use MERGE for Gold  
2. No DQ gates  
3. Left join without orphan policy  
4. No PII handling  
5. Hard-coded paths → Unity Catalog / config  

### Lead DE phrases (use naturally)

- *"I'd filter before the join to cut shuffle."*
- *"For client-facing Gold, I'd enforce the contract in CI."*
- *"Bronze is immutable; corrections happen in Silver upward."*
- *"I'd MERGE on `(client_id, asset_id)` for idempotent daily refresh."*
- *"DQ CRITICAL blocks publish; MEDIUM opens a ticket."*

### Spark performance — top 5

1. Filter early, select only needed columns  
2. Avoid `collect()` on large datasets  
3. Partition by date / `client_id`  
4. Broadcast small dimension tables (`broadcast(df)`)  
5. Enable AQE on Databricks (default on recent DBR)  

### Entity model (quick)

```
CUSTOMER → PROJECT → SITE → ASSET ← INSPECTION → FINDING → WORK_ORDER
                              ↓
                      COMPLIANCE_RESULT ← REGULATION_RULE
```

Gold marts: `gold_asset_risk_kpi`, `gold_compliance_kpi`, `gold_maintenance_sla_kpi`.

### Pre-interview checklist

- [ ] Write `interview_pyspark_example.py` from memory  
- [ ] Explain Bronze / Silver / Gold with one SOCOTEC example each  
- [ ] Recite 3 DQ checks on Gold  
- [ ] Critique `current_pipeline.py` (5 bullets)  
- [ ] Prepare 2 questions for Lead DE  
- [ ] **Business:** TIC + scale (15k / 250k / 26) + Green Trust + one VN/Cementys sentence  
- [ ] **Business:** 2 service lines → 1 data product each (see [§1.8.2](#182-service-lines--data-products-map-for-de-answers))  

---

## 3. Technical Q&A

Answers framed for a **Lead DE** audience: concise, production-oriented, tied to this repo where possible.

### 10-minute quick learn — DE technical mindmaps

> **Mục tiêu:** ôn nhanh 3 nhánh hay hỏi nhất — PySpark live coding, Databricks/DLT, DQ & governance. Mỗi mindmap ~3 phút; chi tiết câu trả lời ở [§A](#a-live-coding--pyspark) · [§B](#b-databricks-delta-lake-dlt) · [§C](#c-data-quality-and-governance).

| Phút | Làm gì | Mindmap / Q |
|------|--------|-------------|
| 0–3 | Nhớ pattern filter → join → groupBy → post-filter | [PySpark](#mindmap-a-pyspark-live-coding) · Q1–Q4 |
| 3–6 | Bronze/Silver/Gold + expectations + MERGE | [DLT & Delta](#mindmap-b-databricks-dlt--delta-lake) · Q5–Q8 |
| 6–10 | Gold DQ + contract + CI gate | [DQ & governance](#mindmap-c-data-quality--governance) · Q9–Q11 |

**Repo khi nói:** `interview_pyspark_example.py` · `proposed_dlt_pipeline.py` · `proposed_data_quality_checks.sql` · `api_contract_example.json`

#### Mindmap A — PySpark (live coding)

```mermaid
mindmap
  root((PySpark Q&A))
    Q1 Aggregates and filters
      Read Silver not Bronze
      Filter early
        status not CANCELLED
        date window 90d
        criticality HIGH CRITICAL
      Inner join on asset_id
      groupBy client_id asset_id
      agg count avg
      Post-filter inspection_count ge 2
      orderBy avg_score desc
      Repo interview_pyspark_example.py
    Q2 DataFrame vs SQL
      Same Catalyst plan
      DataFrame for pipelines DLT tests
      SQL for windows dbt readability
    Q3 Join types
      Inner Gold KPIs matched only
      Left all assets flag gaps
      Left anti DQ zero inspections
      Gap current_pipeline left no orphan policy
    Q4 Skew on client_id
      Salt hot keys
      Two-phase aggregation
      AQE on Databricks
      Partition prune before groupBy
    Cheatsheet patterns
      col count avg when lit
      date_sub current_date
      Window row_number latest per client
    Lead phrases
      Filter before join cut shuffle
      MERGE Gold not daily overwrite
      Explicit alias on agg columns
```

#### Mindmap B — Databricks, DLT & Delta Lake

```mermaid
mindmap
  root((DLT and Delta Q&A))
    Q5 Medallion layers
      Bronze raw append schema drift OK
      Silver conformed dedup pseudonymize
        silver_inspections silver_assets
      Gold KPIs narrow stable
        gold_asset_risk_kpi
      Rule Gold narrow Silver reusable
    Q6 DLT expectations
      expect metric only keep row
      expect_or_drop drop bad rows
      expect_or_fail fail pipeline
      Silver null asset_id inspection_date
      Repo proposed_dlt_pipeline.py
    Q7 MERGE vs OVERWRITE
      Overwrite POC dev rebuild
      MERGE upsert incremental Gold keys
      Append Bronze streams
      Gap current_pipeline overwrite
    Q8 PII pseudonymization
      sha2 concat_ws email country
      Drop raw email column
      Salt in secret manager if needed
      Same hash enables join no expose
      Catalog document inspector_key
    Delta essentials
      format delta append save
      DeltaTable merge whenMatched
      versionAsOf time travel
      OPTIMIZE ZORDER client_id asset_id
    Stack context
      AWS S3 Databricks Airflow
      Unity Catalog ACLs lineage
```

#### Mindmap C — Data quality & governance

```mermaid
mindmap
  root((DQ and Governance Q&A))
    Q9 Gold DQ checks
      Freshness MAX updated_at SLA 1 day
      Null keys client_id asset_id
      Range score 0 to 100
      Plus referential integrity silver_assets
      Row count anomaly vs 7d avg
      No duplicate client_id asset_id
      Repo proposed_data_quality_checks.sql
    Q10 Data contract
      Versioned schema SLA owner security
      api_contract_example.json
      Semver breaking 1.0 to 2.0
      CI validate Gold vs contract pre deploy
      rbac_client_scope row filter client_id
      contains_pii false on Gold products
    Q11 DQ in CI/CD
      PR pipeline change
      Unit tests
      Schema vs contract
      DQ SQL on staging Gold
      Deploy Databricks job
      Freshness alert prod
      Silver DLT expectations
      dbt Great Expectations optional
      CRITICAL block MEDIUM ticket
    Governance pillars
      OpenMetadata catalog
      Unity Catalog schemas ACLs
      Lineage Bronze to Gold
      PII never in client APIs
    Lead trade-off Q18
      MVP Bronze thin Silver one Gold
      Harden contracts DQ RBAC backfill
      Never expose Bronze to clients
```

#### Mindmap tổng hợp — 3 nhánh DE technical (1 trang)

```mermaid
mindmap
  root((SOCOTEC DE Technical 10 min))
    PySpark Q1-Q4
      Filter join groupBy agg
      interview_pyspark_example.py
      Critique current_pipeline joins
    DLT Delta Q5-Q8
      Bronze Silver Gold
      expect_or_drop Silver
      MERGE Gold sha2 PII
      proposed_dlt_pipeline.py
    DQ Governance Q9-Q11
      Freshness nulls range SQL
      Data contract RBAC
      CI block on CRITICAL
      proposed_data_quality_checks.sql
      api_contract_example.json
    Interview hook
      Glassdoor Dec 2025 aggregates filters
      Lead DE production mindset
      TIC inspections to risk KPIs
```

#### Mindmap D — SOCOTEC business (5 min)

```mermaid
mindmap
  root((SOCOTEC Business))
    Company
      TIC global leader
      15k staff 250k clients 26 countries
      Trusted third party lifecycle
    Services
      Green Building TIV
      Fire Environment Safety
      Certification Training
    Digital pillars
      Green Trust BlueTrust
      BIM and Data
      FREEDA AI plans 2026
    Vietnam Cementys
      Structural health monitoring
      Time series 24/7 SLA
      ML SaaS maintenance platform
    Data Hub demand
      AWS Databricks Delta
      Medallion contracts DQ
      Client APIs Power BI GenAI on Gold
    Repo mapping
      gold_asset_risk_kpi
      gold_compliance_kpi
      README section 1.4 to 1.10
```

---

### A. Live coding — PySpark

#### Q1. Write a PySpark query with aggregates and filters.

**Context:** Reported real interview question (Glassdoor, SOCOTEC DE, Dec 2025).

**Prompt restatement:** Given inspection and asset tables, compute client/asset risk KPIs with filters and aggregations.

**Model answer (talk track):**

1. Read from **Silver** (validated) tables, not raw Bronze.
2. **Filter** early: drop `CANCELLED`, restrict date window, keep high-criticality assets.
3. **Join** on `asset_id` with `inner` if you only want matched assets (avoids orphan rows).
4. **GroupBy** business keys: `client_id`, `asset_id`, `criticality_level`.
5. **Aggregate:** `count(inspection_id)`, `avg(non_conformity_score)`.
6. **Post-aggregate filter:** e.g. `inspection_count >= 2` for statistical stability.
7. **Order** by risk metric for top-N use cases.

**Code:** see `src/interview_pyspark_example.py`.

```python
recent = inspections.filter(
    (col("inspection_status") != "CANCELLED")
    & (col("inspection_date") >= date_sub(current_date(), 90))
)

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
```

**Lead-level extras to mention:**

- Push filters before wide joins to reduce shuffle.
- Use explicit `.alias()` instead of default `count(inspection_id)` column names.
- For production Gold, persist to Delta with `merge` keyed on `(client_id, asset_id)` — not daily overwrite.
- Add null guards on score before averaging if source quality is uneven.

---

#### Q2. When do you use `groupBy` + `agg` vs SQL `GROUP BY` in PySpark?

| Approach | Prefer when |
|----------|-------------|
| DataFrame API | Pipeline code, unit tests, DLT/Python notebooks, dynamic column logic |
| Spark SQL | Complex window functions, readable analytics SQL, dbt-style models |

Both compile to the same Catalyst plan. Pick based on team maintainability.

---

#### Q3. Explain join types in the context of inspections ⨝ assets.

| Join | SOCOTEC use case |
|------|------------------|
| **Inner** | Gold KPIs — only assets with at least one inspection |
| **Left** | Audit/reporting — show all assets, flag missing inspections |
| **Left anti** | Data quality — assets with zero inspections in period |

**Repo note:** `current_pipeline.py` uses `left` join but writes a curated snapshot without orphan detection — a gap a Lead would flag.

---

#### Q4. How do you handle skew on `client_id` or `asset_id`?

- Salting hot keys: `concat(col("client_id"), lit("_"), (rand() * num_salts).cast("int")))`.
- Two-phase aggregation: partial agg on salted key, then final agg on real key.
- AQE (Adaptive Query Execution) on Databricks — enable by default on DBR 11+.
- Pre-filter date partitions before groupBy.

---

### B. Databricks, Delta Lake, DLT

#### Q5. Bronze / Silver / Gold — what belongs in each layer at SOCOTEC?

| Layer | Content | SOCOTEC examples |
|-------|---------|------------------|
| **Bronze** | Raw, append-only, source schema + ingest metadata | ERP extracts, inspection app JSON, IoT streams |
| **Silver** | Conformed entities, deduped, pseudonymized, typed | `silver_inspections`, `silver_assets`, `silver_findings` |
| **Gold** | Business KPIs and data products | `gold_asset_risk_kpi`, `gold_compliance_kpi`, client SLA marts |

**Rule:** Gold is narrow and stable; Silver is reusable across domains.

---

#### Q6. What does DLT `@dlt.expect_or_drop` do vs `@dlt.expect`?

| Decorator | Behavior on violation |
|-----------|----------------------|
| `expect` | Record metric, keep row |
| `expect_or_drop` | Drop failing rows |
| `expect_or_fail` | Fail the pipeline update |

**Repo example:** `proposed_dlt_pipeline.py` drops rows with null `asset_id` or `inspection_date` — appropriate for Silver curation.

---

#### Q7. Delta Lake: MERGE vs OVERWRITE for Gold tables?

| Mode | When |
|------|------|
| **Overwrite** | Dev/snapshot rebuilds, idempotent full recompute with partition replace |
| **MERGE (upsert)** | Incremental Gold refresh keyed on `(client_id, asset_id)` |
| **Append** | Bronze event streams, audit logs |

**Lead answer:** `current_pipeline.py` uses overwrite — fine for POC; production Gold should MERGE with `updated_at` tracking and backward-compatible schema evolution.

---

#### Q8. How do you pseudonymize inspector PII in Silver?

**Repo pattern:**

```python
sha2(concat_ws("||", col("inspector_email"), col("country_code")), 256)
```

Then drop `inspector_email`. Mention:

- Salt/pepper stored in secret manager if reversibility is never needed.
- Same input → same hash enables joinability without exposing PII.
- Document in catalog: `inspector_key` is derived, not raw PII.

---

### C. Data quality and governance

#### Q9. What quality checks would you run on `gold_asset_risk_kpi`?

From `proposed_data_quality_checks.sql`:

1. **Freshness** — `MAX(updated_at)` within SLA window (daily → 1 day).
2. **Null keys** — `client_id`, `asset_id` must never be null.
3. **Range** — `avg_non_conformity_score` between 0 and 100.

**Add for Lead depth:**

- Referential integrity: every `asset_id` exists in `silver_assets`.
- Row count anomaly vs 7-day rolling average.
- Duplicate keys on `(client_id, asset_id)`.

---

#### Q10. What is a data contract and why does SOCOTEC need one for client APIs?

A versioned agreement between producer and consumer: schema, SLA, ownership, security.

**Repo example:** `api_contract_example.json` defines fields, refresh frequency, availability, RBAC policy.

**Lead points:**

- Breaking changes require semver bump (`1.0.0` → `2.0.0`).
- CI validates Gold schema against contract before deploy.
- Client-scoped access: `rbac_client_scope` — row filter on `client_id`.

---

#### Q11. How do you integrate DQ into CI/CD?

```mermaid
flowchart LR
    PR["PR: pipeline change"] --> UT["Unit tests"]
    UT --> SC["Schema vs contract"]
    SC --> DQ["DQ SQL checks on staging Gold"]
    DQ --> DEP["Deploy Databricks job"]
    DEP --> MON["Freshness alert in prod"]

    classDef step fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20
    class PR,UT,SC,DQ,DEP,MON step
```

- dbt tests / Great Expectations / DLT expectations at Silver.
- SQL checks (like repo sample) post-Gold build in staging.
- Block promote on CRITICAL; warn on MEDIUM.

---

### D. Architecture and ingestion

#### Q12. Batch vs streaming for SOCOTEC sources?

| Source | Pattern | Why |
|--------|---------|-----|
| ERP / CRM | Batch or CDC (Fivetran) | Predictable volumes, snapshot correctness |
| Inspection mobile apps | Micro-batch or Kafka → Bronze | Near-real-time ops dashboards |
| IoT sensors | Streaming (Structured Streaming) | High velocity, anomaly detection |

**Medallion stays the same** — streaming lands Bronze; Silver/Gold can be batch or streaming DLT.

---

#### Q13. How would Airflow orchestrate this stack?

- DAG tasks: ingest → trigger Databricks job (DLT or notebook) → run DQ SQL → notify on failure.
- Use `DatabricksSubmitRunOperator` with job clusters or existing all-purpose policy.
- Separate DAGs per domain (inspections vs compliance) with dataset-driven scheduling (Airflow 2.4+).
- SLA sensors on Gold freshness — page if `gold_asset_risk_kpi` stale > 25h.

---

#### Q14. Critique `current_pipeline.py` — what would you change?

| Issue | Fix |
|-------|-----|
| No DQ | DLT expectations or pre-write validation |
| `overwrite` on curated path | Partitioned Delta MERGE |
| Left join without orphan handling | Inner for KPIs; separate DQ report for unmatched |
| No PII treatment | Pseudonymize in Silver |
| No lineage/audit columns | `updated_at`, `_source_file`, `_ingest_ts` |
| Hard-coded S3 paths | Parameterize via config / Unity Catalog volumes |

This is a strong "code review" answer for a Lead round.

---

### E. SOCOTEC business and domain

#### Q15. How does data engineering support SOCOTEC's TIC business?

**Value chain:** field inspection → measurements/reports → compliance evidence → client risk recommendations → **recurring data products**.

**Engineering enablers:**

- Unified asset and inspection master data (Silver).
- Compliance KPI marts tied to regulation rules.
- Client APIs for asset health and ESG reporting.
- GenAI over **certified Gold metrics** (not raw Bronze).

---

#### Q16. Name 2–3 monetizable data products for SOCOTEC clients.

1. **Asset risk dashboard** — `gold_asset_risk_kpi` (inspection frequency, non-conformity trends).
2. **Compliance automation API** — pass/fail against regulation rules with evidence links.
3. **Predictive maintenance signals** — feature store from inspection findings + IoT (MLOps layer).
4. **Monitoring / Green Trust SaaS** — real-time structural or environmental KPIs with SLA-backed freshness (Cementys-style).
5. **ESG / low-carbon trajectory** — energy optimization benchmarks (e.g. asset-management clients like PERIAL).

---

#### Q20. Describe SOCOTEC’s business model without jargon.

SOCOTEC sells **trust**: independent experts test, inspect, and certify that buildings, infrastructure, and industrial assets meet safety, regulatory, and sustainability requirements. Clients are owners, contractors, insurers, and public bodies. Revenue is project-based and recurring (re-inspections, monitoring contracts, certification audits). The group is scaling **digital** layers — monitoring platforms, BIM-linked data, AI-assisted document analysis — so the Data Hub can productize the same evidence clients already pay for in PDFs and reports.

---

#### Q21. What are Green Trust and BlueTrust Monitoring?

**Green Trust** is SOCOTEC’s umbrella for environmentally and structurally **sustainable, monitored assets**. **BlueTrust Monitoring** covers environmental monitoring (e.g. water quality — relevant to UK/NL public contracts). For DE: treat sensor and lab feeds as **high-volume Bronze**, roll up to Gold KPIs with strict freshness SLAs; never mix unvalidated raw streams into client APIs.

---

#### Q22. How do acquisitions affect the data platform?

Recent moves (testing labs, geodata, monitoring, infrastructure consultancies — US, UK, Germany, Italy) bring **new source systems**. Pattern: land in Bronze per source → **Silver conformation** on shared keys (`asset_id`, `client_id`, `site_id`) → single Gold product per client contract. Avoid N duplicate Gold tables per acquisition; merge in Silver.

---

#### Q23. BIM & Data — what should a DE know?

BIM links **3D model components** to project phases. SOCOTEC’s angle is assurance data tied to assets (inspections, monitoring points, compliance). Silver should hold a **stable asset registry** that BIM tools and monitoring dashboards both reference; Gold exposes KPIs, not full BIM geometry (store references/IDs).

---

#### Q24. Why is Vietnam (Cementys) strategically important?

VN is the **monitoring and digital-platform** beachhead: structural health for transport/energy, environmental measurements, ML/SaaS maintenance. Data Hub needs **low-latency, reliable pipelines** for time-series and shared asset masters — your role bridges Massy lakehouse standards and VN engineering consumers (relevant if Viet interviews).

---

#### Q25. Map one UAE mega-project to data entities.

Public projects: Louvre Abu Dhabi, Sea World, DEWA, Etihad Rail. Services: third-party design review, inspections, H&S, MEP. In the lakehouse: **PROJECT → SITE → ASSET**, inspections and **COMPLIANCE_RESULT** with `evidence_link`, client-scoped Gold for portfolio risk — aligns with repo ER model in README §4.

---

### F. Lead DE — design and behavior

#### Q17. A client reports KPI mismatch vs their internal records. Your process?

1. Confirm contract version and refresh timestamp.
2. Reconcile row counts and key sets (`client_id`, `asset_id`) for the period.
3. Trace lineage: Gold → Silver → Bronze → source extract.
4. Check for filter differences (e.g. they include `CANCELLED`, you exclude).
5. Document root cause; fix pipeline or clarify contract; communicate SLA for correction.

---

#### Q18. How do you balance delivery speed vs governance on a new client onboarding?

- **MVP:** Bronze + thin Silver + one Gold KPI with manual DQ sign-off.
- **Hardening sprint:** contracts, automated DQ, RBAC, backfill playbook.
- Never expose Bronze to clients; never skip PII review for external products.

---

#### Q19. How would you mentor a junior DE on this codebase?

- Pair on one vertical slice: Bronze → Silver for one entity.
- Review PRs for filter-before-join, explicit aliases, test data.
- Have them write one DQ check and one contract field doc before merging Gold change.

---

### G. Quick-fire (short answers)

| Question | Answer |
|----------|--------|
| **Partition Gold by?** | `client_id` + date (or `updated_at` date) for prune and RBAC |
| **Z-order on Delta?** | High-cardinality filter columns: `client_id`, `asset_id` |
| **Unity Catalog role?** | Central governance: schemas, ACLs, lineage, external locations |
| **Idempotent pipeline?** | Deterministic keys + MERGE; ingest dedup on `(source_id, event_ts)` |
| **PII in Gold?** | No — repo contract sets `contains_pii: false` |
| **Power BI connection?** | DirectQuery or Import from Databricks SQL / Gold tables |
| **Cost control on Databricks?** | Job clusters, auto-termination, partition pruning, avoid `collect()` |

---

## 4. Questions to ask the Lead DE

Pick 2–3 — shows senior curiosity without interrogating:

1. *"What is the current split between batch and streaming pipelines in the international Lakehouse?"*
2. *"How does the team enforce data contracts today — CI, DLT expectations, or catalog policies?"*
3. *"What does 'done' look like for a Gold data product before it goes to a client API or Power BI?"*
4. *"Where do you see GenAI (GenIE / NL-to-SQL) fitting vs traditional semantic layers?"*
5. *"What would success look like for this role in the first 90 days?"*
