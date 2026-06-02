# SOCOTEC DE technical interview — Lead DE round

> **Audience:** Lead Data Engineer interviewer at SOCOTEC Data & AI Hub (Massy, Ile-de-France).  
> **Case study repo:** [`../../README.md`](../../README.md) · Code samples: [`../../src/`](../../src/)

---

## 0. Round strategy

| Signal the Lead DE looks for | How to demonstrate |
|------------------------------|-------------------|
| **PySpark fluency** | Write clean aggregates + filters on inspection/asset data without IDE autocomplete |
| **Production mindset** | Mention DQ gates, idempotency, backfill, SLA, cost — not just "make it work" |
| **Lakehouse literacy** | Bronze/Silver/Gold, Delta, DLT expectations, merge vs overwrite trade-offs |
| **Governance awareness** | PII pseudonymization, data contracts, client-scoped RBAC |
| **Business framing** | Tie answers to TIC value chain: inspections → compliance → client risk KPIs |
| **Senior judgment** | Trade-offs, when to stop perfecting, how you'd mentor a mid-level DE |

**Core message:** You understand SOCOTEC's stack (AWS + Databricks + Delta + Airflow) and can move their inspection/compliance data from raw landing to governed client-facing products.

---

## 1. Opening pitch (60 seconds)

> I'm a data engineer focused on lakehouse platforms — Spark, Delta Lake, and medallion pipelines on AWS. I've studied SOCOTEC's TIC business and Data & AI Hub direction: turning field inspection and compliance data into recurring analytics products — asset risk KPIs, compliance dashboards, client APIs.  
>  
> This repo is my working blueprint: a current-style Spark ETL, a proposed DLT pipeline with quality expectations, Gold-layer SQL checks, and an API contract example. I'm ready to go deep on PySpark, pipeline design, and how we'd harden this for production at SOCOTEC scale.

---

## 2. How to use this repo in the interview

| If they ask… | Point to… |
|--------------|-----------|
| "Walk me through your understanding of our data platform" | README §2 Architecture + §1 Business |
| "What's wrong with a simple ETL?" | `src/current_pipeline.py` — no DQ, left join fan-out risk, overwrite mode, no PII handling |
| "How would you improve it?" | `src/proposed_dlt_pipeline.py` — expectations, pseudonymization, Gold aggregation |
| "How do you validate Gold tables?" | `src/proposed_data_quality_checks.sql` |
| "How do external clients consume data?" | `src/api_contract_example.json` |
| Live PySpark coding | `src/interview_pyspark_example.py` + [`02-cheatsheet.md`](02-cheatsheet.md) § PySpark |

---

## 3. Likely interview flow (based on public reports + Lead DE profile)

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

---

## 4. Before the call — 30-minute drill

1. **Read** [`02-cheatsheet.md`](02-cheatsheet.md) once (10 min).
2. **Write from memory** the PySpark example in `src/interview_pyspark_example.py` on paper or a blank notebook (10 min).
3. **Explain aloud** why `current_pipeline.py` is insufficient and how DLT fixes it (5 min).
4. **Prepare 3 questions** for the Lead DE (see [`01-technical-qa.md`](01-technical-qa.md) § Questions to ask).

---

## 5. Questions to ask the Lead DE

Pick 2–3 — shows senior curiosity without interrogating:

1. *"What is the current split between batch and streaming pipelines in the international Lakehouse?"*
2. *"How does the team enforce data contracts today — CI, DLT expectations, or catalog policies?"*
3. *"What does 'done' look like for a Gold data product before it goes to a client API or Power BI?"*
4. *"Where do you see GenAI (GenIE / NL-to-SQL) fitting vs traditional semantic layers?"*
5. *"What would success look like for this role in the first 90 days?"*

---

## 6. File map

| File | Purpose |
|------|---------|
| [`01-technical-qa.md`](01-technical-qa.md) | Full Q&A with model answers |
| [`02-cheatsheet.md`](02-cheatsheet.md) | Syntax and pattern quick reference |
| [`../../src/interview_pyspark_example.py`](../../src/interview_pyspark_example.py) | Live-coding reference (Glassdoor-style question) |
