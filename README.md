# SOCOTEC Client Data Solution

This repository proposes a practical data strategy and engineering blueprint for SOCOTEC's client-facing data platform, aligned with its TIC (Testing, Inspection, Certification) business and current Data & AI Hub direction.

## 1) Business

### 1.1 Current Business Model (TIC + Data-Driven Services)
- Core business: testing, inspection, certification, and technical advisory services for construction, infrastructure, environment, and safety.
- Value chain: field operations -> measurements/reports -> compliance evidence -> risk reduction recommendations for clients.
- Data opportunity: convert inspection and operations data into recurring digital products (predictive maintenance, risk scoring, compliance dashboards, client APIs).
- Strategic fit: SOCOTEC already operates a global Data & AI Hub and is modernizing an international Lakehouse.

### 1.2 Quick Revenue / Profitability Snapshot (Recent Years)
Based on public SOCOTEC sustainability reports:
- 2023 revenue: EUR 1,308.5M; EBITDA: EUR 223M; EBITDA margin: ~17%.
- 2024 revenue: EUR 1,476.6M; EBITDA: EUR 306.4M; EBITDA margin: ~20.7%.
- YoY trend: strong growth in both top-line and operating profitability, supported by organic growth and acquisitions.

Sources:
- [SOCOTEC Sustainability Report 2023](https://static.socotec.com/s3fs-public/2024-10/190624-en-csr-report-socotec-2023-finaljune24-002_0.pdf)
- [SOCOTEC Sustainability Report 2024](https://static.socotec.co.uk/s3fs-public/2025-06/socotec-group-sustainability-report-2024.pdf)

### 1.3 Potential Assessment
SOCOTEC has high potential to scale data products because:
- Large installed base of industrial/building/infrastructure projects generates defensible proprietary datasets.
- Existing Lakehouse and cloud data capabilities reduce time-to-market for analytics products.
- Demand for compliance automation, cost optimization, predictive maintenance, and ESG reporting is rising.
- GenAI (e.g., Databricks GenIE) can improve self-service insights for client and internal teams.

Overall assessment: **High potential**, especially for monetizable B2B analytics and AI-assisted risk management offerings.

### 1.4 Company Snapshot (Public, ~2025–2026)

| Metric | Value |
|--------|-------|
| Positioning | Global leader in **Testing, Inspection, Certification (TIC)** for construction, infrastructure, and industry |
| Tagline | *Building trust for a safer and sustainable world* |
| Scale | ~**15,000** employees · **250,000** clients · **26** countries |
| Operating model | **Trusted third party** — public and private clients, full project lifecycle (design → operation → decommissioning) |

**Strategic themes (corporate site):** Renewable energy · Sustainability · Smart cities · Industry 4.0 · **BIM & Data**

### 1.5 Service Lines (What SOCOTEC Sells)

| Service line | Typical deliverables | Data relevance |
|--------------|---------------------|----------------|
| **Green Building** | Energy performance, low-carbon trajectories, ESG | Time-series energy, asset benchmarks, carbon KPIs |
| **Technical Inspection & Verification (TIV)** | Regulatory inspections, periodic facility/equipment checks | Inspection events, pass/fail, schedules, evidence |
| **Specialty Engineering** | Structural, geotechnical, envelope, dispute support | Models, measurements, lab results |
| **Failure Analysis** | Root cause, forensic engineering | Case files, sensor logs, reports |
| **Fire & Life Safety** | Testing, certification, building control (e.g. UKTC acquisition) | Compliance results, test certificates |
| **Environment & Safety** | Monitoring, hygiene, water quality, asbestos | Environmental samples, thresholds, alerts |
| **Certification** | ISO / FSSC / GHG verification (strong in APAC hubs) | Audit trails, management-system metadata |
| **Training** | 41 training centres in France alone | LMS data, certification renewals |

### 1.6 Sectors & Client Types

| Sector | Examples | SOCOTEC role |
|--------|----------|--------------|
| **Construction & Real Estate** | Buildings, envelopes, materials testing | Risk reduction before/after handover |
| **Infrastructure** | Roads, dams, rail (e.g. Etihad Rail UAE), ordnance (Germany) | Long-life asset monitoring and safety |
| **Industry & Energy** | Plants, utilities, renewable (Harvard Street solar, dams) | Compliance + performance optimization |
| **Real Estate / Asset owners** | PERIAL energy optimization, property valuations (NL) | Recurring advisory + monitoring contracts |

### 1.7 Product Families: Green Trust & Trust & Tech

**Green Trust** — environmental and structural assurance for sustainable assets:

- **BlueTrust Monitoring** — environmental monitoring (water, air, soil)
- **Optic fibre / structural monitoring** — deformation, structural health
- **Topographic surveys** — geospatial baseline for change detection

**Trust & Tech / BIM & Data** — digital layer on physical inspections:

- BIM-linked asset models and project data
- **Integrated digital platform** (Vietnam Cementys): survey software, real-time monitoring SaaS, ML/AI for infrastructure ageing
- Partnerships: e.g. **FREEDA** (AI architectural plan analysis, Jan 2026)

*DE implication:* Bronze = raw sensor/app/ERP feeds; Silver = conformed assets + time-series; Gold = client KPIs (risk, compliance, freshness, anomaly flags) consumed by monitoring UIs and APIs.

### 1.8 Regional Footprint (Interview Context)

| Region | Note | Scale (public) |
|--------|------|----------------|
| **France** | Group HQ strength; 190 branches, 41 training centres | Leader in TIC risk management |
| **UK & Ireland** | Materials testing, environmental monitoring, acquisitions (LDG, UKTC) | 2,300+ experts, 65 offices |
| **USA** | Building envelope, geotech, commissioning, dispute resolution | 1,700 experts, 40+ offices |
| **Germany** | Building, infrastructure, EOD (Röhll & Koch), geodata (TRIGIS) | 1,500 employees, 38 locations |
| **Spain / BAC** | Civil engineering inspection, labs in Catalonia | 850 employees |
| **Vietnam (Cementys)** | **Structural health monitoring**, environmental services, digital platform | 1 office; ties to global monitoring + Data Hub |
| **UAE** | Mega-projects (Louvre Abu Dhabi, Sea World, DEWA, Etihad Rail) | Third-party design review, MEP, H&S |
| **APAC certification** | Singapore, Japan, Thailand, Philippines — ISO, GHG, concrete/steel cert | Management-system audits |

### 1.9 Vietnam — Cementys & Monitoring (Vu Tran-Viet Round)

SOCOTEC Vietnam operates through **Cementys**, focused on **tech-enabled monitoring** (not generic TIC back-office):

- In-situ measurements: technical assessment, inspections, surveys
- **Structural health monitoring** for transport and energy infrastructure
- Environmental: noise, vibration, water pollution, geotechnical, topography
- **Data visualisation**: proprietary survey/maintenance software, 24/7 on-call monitoring
- **Digital platform**: data science, automated ageing analysis, maintenance SaaS, ML/AI

**What they likely need from a DE:** reliable ingestion of high-frequency sensor streams, asset master alignment, SLA-backed Gold metrics for dashboards/BIM, clear ownership between Massy Data Hub and VN engineering.

### 1.10 Data & AI Hub — Inferred Role Requirements

From public job posts, LinkedIn (e.g. Lead DE Perrine TCHEEKO), and group digital direction:

| Requirement area | Expected depth |
|------------------|----------------|
| **PySpark / SQL** | Aggregates, filters, joins; live coding reported (Glassdoor, Dec 2025) |
| **Lakehouse** | AWS + **Databricks** + **Delta**; Bronze/Silver/Gold; DLT expectations |
| **Orchestration** | Airflow; job triggers, SLA sensors |
| **Governance** | PII/GDPR, Unity Catalog, data contracts, DQ in CI |
| **Product mindset** | Turn inspection/compliance/monitoring data into **client-facing products** (APIs, Power BI, GenAI on Gold only) |
| **Soft signals** | Documentation, teamwork, bilingual hub (FR/EN), production escalation judgment |

**Business pull:** acquisitions (testing labs, monitoring, geodata) increase heterogeneous sources → need standardized Silver entities and governed Gold products.

### 1.11 Business Visuals (Mermaid)
```mermaid
flowchart TB
    A[Field Inspection and Testing] --> B[Reports and Measurements]
    B --> C[Compliance Evidence]
    C --> D[Client Risk Recommendations]
    D --> E[Recurring Data Products]

    classDef ops fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px,color:#0D47A1;
    classDef value fill:#E8F5E9,stroke:#43A047,stroke-width:2px,color:#1B5E20;
    classDef product fill:#FFF3E0,stroke:#FB8C00,stroke-width:2px,color:#E65100;
    class A,B,C,D ops;
    class E product;
```

```mermaid
flowchart TB
    R23["2023 Revenue: 1308.5M EUR"] --> R24["2024 Revenue: 1476.6M EUR"]
    R24 --> G1["Revenue Growth: +12.8%"]
    E23["2023 EBITDA: 223.0M EUR"] --> E24["2024 EBITDA: 306.4M EUR"]
    E24 --> G2["EBITDA Margin: 17.0% to 20.7%"]

    classDef revenue fill:#E8EAF6,stroke:#3949AB,stroke-width:2px,color:#1A237E;
    classDef ebitda fill:#E0F7FA,stroke:#00838F,stroke-width:2px,color:#004D40;
    classDef growth fill:#FFFDE7,stroke:#F9A825,stroke-width:2px,color:#F57F17;
    class R23,R24 revenue;
    class E23,E24 ebitda;
    class G1,G2 growth;
```

## 2) Architecture

### 2.1 Current Data Solution (Likely Baseline from JD Context)
Current stack direction in job posts and profiles indicates:
- Cloud: AWS-first data platform.
- Lakehouse: Databricks + Delta Lake + S3.
- Ingestion: Fivetran/Airbyte + custom connectors.
- Processing: Spark batch/stream workloads.
- Orchestration: Airflow.
- BI/Serving: Power BI and Databricks SQL.
- Governance/metadata: OpenMetadata style catalog + data quality controls.
- Collaboration: Git/GitLab, notebooks, CI/CD.

### 2.2 Proposed Target Data Solution for Clients
#### A. Ingestion Layer
- Sources: ERP, CRM, IoT sensors, inspection apps, external regulatory/open data.
- Pattern: CDC + batch + event streams (Kafka).
- Contracts: schema registry and source-level data contracts.

#### B. Lakehouse Medallion
- Bronze: immutable raw landing, source lineage, minimal validation.
- Silver: standardized entities (assets, inspections, incidents, work orders) with pseudonymization.
- Gold: domain marts (Asset Health, Compliance KPI, Cost/Risk, ESG, Client SLAs).

#### C. Data Governance & Trust
- Data quality tests (freshness, null checks, referential integrity, business rules).
- PII handling with tokenization/hashing and row/column-level access policy.
- Lineage, ownership, and SLA enforcement integrated in CI/CD.

#### D. Serving & Product Layer
- BI dashboards for business users.
- API/data products for client integration.
- Semantic layer and query acceleration for self-service analytics.
- GenAI assistant (NL-to-SQL + retrieval over certified metrics).

#### E. DataOps/MLOps
- CI/CD for pipelines and SQL models.
- Observability: pipeline health, data incidents, cost monitoring.
- Versioned data products and backward-compatible contracts.

### 2.3 Reference Architecture (Text)
1. Sources -> 2. Ingestion (CDC/Batch/Streaming) -> 3. Bronze (S3/Delta) -> 4. Silver transformations (Spark/dbt) -> 5. Gold marts + feature sets -> 6. Consumption (Power BI, Databricks SQL, APIs, GenAI assistant) -> 7. Governance/Monitoring across all layers.

### 2.4 Architecture Visuals (Mermaid)
```mermaid
flowchart TB
    ERP[ERP and Finance] --> CDC[CDC Connectors]
    CRM[CRM and Sales] --> CDC
    IOT[IoT Sensors] --> STREAM[Kafka Streams]
    APP[Inspection Apps] --> BATCH[Batch ELT Jobs]
    EXT[External Data] --> BATCH
    CDC --> BRONZE[Bronze Raw Delta]
    STREAM --> BRONZE
    BATCH --> BRONZE

    classDef src fill:#EDE7F6,stroke:#5E35B1,stroke-width:2px,color:#311B92;
    classDef ing fill:#E1F5FE,stroke:#039BE5,stroke-width:2px,color:#01579B;
    classDef med fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px,color:#4A148C;
    class ERP,CRM,IOT,APP,EXT src;
    class CDC,BATCH,STREAM ing;
    class BRONZE med;
```

```mermaid
flowchart TB
    BRONZE[Bronze Raw Delta] --> SILVER[Silver Curated Delta]
    SILVER --> GOLD[Gold Business Marts]

    classDef med fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px,color:#4A148C;
    class BRONZE,SILVER,GOLD med;
```

```mermaid
flowchart TB
    GOLD[Gold Business Marts] --> BI[BI Dashboards]
    GOLD --> API[Client APIs]
    GOLD --> GENAI[GenAI Assistant]

    classDef med fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px,color:#4A148C;
    classDef con fill:#FFF8E1,stroke:#F9A825,stroke-width:2px,color:#F57F17;
    class GOLD med;
    class BI,API,GENAI con;
```

```mermaid
flowchart TB
    subgraph GOV[Governance and Trust]
        Q1[Freshness and Completeness Checks]
        Q2[Schema Validation and Contracts]
        Q3[PII Pseudonymization]
        Q4[Lineage and Ownership]
        Q5[SLA Monitoring and Alerts]
    end

    BR[Bronze] --> SI[Silver] --> GO[Gold]
    GOV -. policy and controls .-> BR
    GOV -. policy and controls .-> SI
    GOV -. policy and controls .-> GO

    classDef control fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20;
    classDef data fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,color:#E65100;
    class Q1,Q2,Q3,Q4,Q5 control;
    class BR,SI,GO data;
```

```mermaid
sequenceDiagram
    autonumber
    participant U as Client User
    participant G as GenAI Assistant
    participant M as Metrics Layer
    participant D as Databricks SQL
    participant R as Risk KPI Mart

    U->>G: "Top 10 assets with highest risk this month"
    G->>M: Resolve certified metric and dimensions
    M->>D: Generate governed SQL query
    D->>R: Execute query on Gold mart
    R-->>D: Return aggregated result
    D-->>G: Structured answer payload
    G-->>U: Insight + explanation + filter tips
```

## 3) Engineering Code

### 3.1 Sample of "Current Style" (Typical Spark ETL)
See: `src/current_pipeline.py`
- Simple ingestion + transformation pattern.
- Minimal data quality and no contract enforcement.

### 3.2 Proposed Engineering Code for Target Architecture
See files:
- `src/proposed_dlt_pipeline.py` -> Medallion-style transformation with data quality expectations.
- `src/proposed_data_quality_checks.sql` -> SQL quality checks for Gold marts.
- `src/api_contract_example.json` -> Data product contract for external clients.

### 3.3 Why This Engineering Proposal
- Improves reliability: explicit contracts + quality gates.
- Improves governance: standardized pseudonymization and lineage-ready design.
- Improves business value: reusable data products and faster client analytics delivery.
- Improves scalability: modular pipelines compatible with Databricks, Spark, and CI/CD workflows.

### 3.4 Engineering Delivery Visual (Mermaid)
```mermaid
flowchart TB
    DEV[Data Engineer Commit] --> CI[CI: Unit + SQL + DQ Tests]
    CI --> BUILD[Build Artifacts]
    BUILD --> DEPLOY[Deploy to Databricks Jobs/DLT]
    DEPLOY --> OBS[Observability and Data Incident Alerts]
    OBS --> FEED[Feedback to Backlog]
    FEED --> DEV

    classDef dev fill:#E3F2FD,stroke:#1565C0,stroke-width:2px,color:#0D47A1;
    classDef ci fill:#F1F8E9,stroke:#689F38,stroke-width:2px,color:#33691E;
    classDef run fill:#FCE4EC,stroke:#C2185B,stroke-width:2px,color:#880E4F;
    class DEV,FEED dev;
    class CI,BUILD ci;
    class DEPLOY,OBS run;
```

### 3.5 Main File Internals Visuals (Mermaid)

#### A. `src/current_pipeline.py` (`run()` flow)
```mermaid
flowchart TD
    S["Start: run"] --> SP["Create SparkSession"]
    SP --> RI[Read inspections parquet]
    SP --> RA[Read assets parquet]
    RI --> J[Left join on asset_id]
    RA --> J
    J --> F[Filter inspection_status != CANCELLED]
    F --> T[Add processed_at timestamp]
    T --> W[Write Delta to curated snapshot path]
    W --> E["End"]

    classDef io fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px,color:#0D47A1;
    classDef trans fill:#E8F5E9,stroke:#43A047,stroke-width:2px,color:#1B5E20;
    classDef out fill:#FFF3E0,stroke:#FB8C00,stroke-width:2px,color:#E65100;
    class SP,RI,RA io;
    class J,F,T trans;
    class W out;
```

#### B. `src/proposed_dlt_pipeline.py` (DLT tables and methods)
```mermaid
flowchart TB
    B1["Read stream bronze_inspections"] --> B2["Expectation asset_id not null"]
    B2 --> B3["Expectation inspection_date not null"]
    B3 --> B4["Create hashed inspector_key"]
    B4 --> B5["Drop inspector_email column"]
    B5 --> B6["Add updated_at timestamp"]
    B6 --> B7["Output DLT table silver_inspections"]

    classDef silver fill:#EDE7F6,stroke:#5E35B1,stroke-width:2px,color:#311B92;
    class B1,B2,B3,B4,B5,B6,B7 silver;
```

```mermaid
flowchart TB
    G1["Read DLT table silver_inspections"] --> G3["Inner join on asset_id"]
    G2["Read table silver_assets"] --> G3
    G3 --> G4["Group by client and asset"]
    G4 --> G5["Aggregate inspection_id count"]
    G5 --> G6["Aggregate non_conformity_score average"]
    G6 --> G7["Rename final KPI columns"]
    G7 --> G8["Output DLT table gold_asset_risk_kpi"]

    classDef gold fill:#FFF8E1,stroke:#F9A825,stroke-width:2px,color:#F57F17;
    class G1,G2,G3,G4,G5,G6,G7,G8 gold;
```

#### C. `src/proposed_data_quality_checks.sql` (query checks)
```mermaid
flowchart TB
    Q1[Check 1: Freshness] --> R1{Updated in last 1 day}
    R1 -->|Yes| P1[PASS]
    R1 -->|No| F1[FAIL]

    Q2[Check 2: Null keys] --> R2[Count rows with null client_id or asset_id]
    R2 --> A2[Alert if count > 0]

    Q3[Check 3: Score threshold] --> R3[Count rows with score outside 0 to 100]
    R3 --> A3[Alert if count > 0]

    classDef check fill:#E0F7FA,stroke:#00838F,stroke-width:2px,color:#004D40;
    classDef ok fill:#E8F5E9,stroke:#2E7D32,stroke-width:2px,color:#1B5E20;
    classDef bad fill:#FFEBEE,stroke:#C62828,stroke-width:2px,color:#B71C1C;
    classDef act fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,color:#E65100;
    class Q1,Q2,Q3,R1,R2,R3 check;
    class P1 ok;
    class F1 bad;
    class A2,A3 act;
```

#### D. `src/api_contract_example.json` (contract structure)
```mermaid
flowchart TB
    ROOT["client_asset_risk_kpi contract"] --> M["Metadata"]
    ROOT --> S["SLA"]
    ROOT --> F["Fields"]
    ROOT --> SEC["Security"]

    classDef root fill:#E8EAF6,stroke:#3949AB,stroke-width:2px,color:#1A237E;
    classDef group fill:#E0F7FA,stroke:#00838F,stroke-width:2px,color:#004D40;
    class ROOT root;
    class M,S,F,SEC group;
```

```mermaid
flowchart TB
    M["Metadata"] --> M1["product_name"]
    M --> M2["version"]
    M --> M3["owner_team"]

    S["SLA"] --> S1["refresh_frequency daily"]
    S --> S2["availability 99.5%"]

    classDef group fill:#E0F7FA,stroke:#00838F,stroke-width:2px,color:#004D40;
    classDef leaf fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,color:#E65100;
    class M,S group;
    class M1,M2,M3,S1,S2 leaf;
```

```mermaid
flowchart TB
    F["Fields"] --> F1["client_id string"]
    F --> F2["asset_id string"]
    F --> F3["criticality_level string"]
    F --> F4["inspection_count long"]
    F --> F5["avg_non_conformity_score double"]
    F --> F6["updated_at timestamp"]

    classDef group fill:#E0F7FA,stroke:#00838F,stroke-width:2px,color:#004D40;
    classDef leaf fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,color:#E65100;
    class F group;
    class F1,F2,F3,F4,F5,F6 leaf;
```

```mermaid
flowchart TB
    SEC["Security"] --> SC1["contains_pii false"]
    SEC --> SC2["access_policy rbac_client_scope"]

    classDef group fill:#E0F7FA,stroke:#00838F,stroke-width:2px,color:#004D40;
    classDef leaf fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,color:#E65100;
    class SEC group;
    class SC1,SC2 leaf;
```

## 4) Data Model (DB Diagram)

This section visualizes the main business entities SOCOTEC can maintain to support client-facing analytics, compliance, and operations.

### 4.1 Core Master Data (Customer, Site, Asset, Inspector)
```mermaid
erDiagram
    CUSTOMER ||--o{ PROJECT : owns
    PROJECT ||--o{ SITE : contains
    SITE ||--o{ ASSET : hosts
    CUSTOMER ||--o{ CONTRACT : signs
    CONTRACT ||--o{ PROJECT : governs
    INSPECTOR ||--o{ INSPECTION : performs

    CUSTOMER {
      string customer_id PK
      string customer_name
      string industry_type
      string country_code
      string account_tier
    }

    CONTRACT {
      string contract_id PK
      string customer_id FK
      date start_date
      date end_date
      string sla_level
      string status
    }

    PROJECT {
      string project_id PK
      string customer_id FK
      string contract_id FK
      string project_name
      string project_type
      string status
    }

    SITE {
      string site_id PK
      string project_id FK
      string site_name
      string region
      float latitude
      float longitude
    }

    ASSET {
      string asset_id PK
      string site_id FK
      string asset_type
      string criticality_level
      date commissioning_date
      string lifecycle_status
    }

    INSPECTOR {
      string inspector_id PK
      string inspector_key
      string team_name
      string certification_level
      string country_code
    }
```

### 4.2 Inspection, Findings, Actions, Compliance
```mermaid
erDiagram
    ASSET ||--o{ INSPECTION : receives
    INSPECTION ||--o{ INSPECTION_FINDING : produces
    INSPECTION_FINDING ||--o{ WORK_ORDER : triggers
    INSPECTION ||--o{ COMPLIANCE_RESULT : evaluates
    REGULATION_RULE ||--o{ COMPLIANCE_RESULT : checks
    WORK_ORDER ||--o{ WORK_ORDER_EVENT : tracks

    INSPECTION {
      string inspection_id PK
      string asset_id FK
      string inspector_id FK
      datetime inspection_ts
      string inspection_method
      string inspection_status
      double non_conformity_score
    }

    INSPECTION_FINDING {
      string finding_id PK
      string inspection_id FK
      string severity_level
      string finding_category
      string description
      bool is_critical
    }

    WORK_ORDER {
      string work_order_id PK
      string finding_id FK
      string assigned_team
      date due_date
      string priority
      string work_order_status
    }

    WORK_ORDER_EVENT {
      string event_id PK
      string work_order_id FK
      datetime event_ts
      string event_type
      string event_note
    }

    REGULATION_RULE {
      string rule_id PK
      string country_code
      string domain
      string rule_code
      string rule_version
    }

    COMPLIANCE_RESULT {
      string compliance_result_id PK
      string inspection_id FK
      string rule_id FK
      string compliance_status
      string evidence_link
      datetime evaluated_ts
    }
```

### 4.3 Analytics and Client Reporting Layer
```mermaid
flowchart TB
    INSPECTION[inspection facts] --> GOLD1[gold_asset_risk_kpi]
    INSPECTION_FINDING[finding facts] --> GOLD1
    WORK_ORDER[work order facts] --> GOLD2[gold_maintenance_sla_kpi]
    COMPLIANCE_RESULT[compliance facts] --> GOLD3[gold_compliance_kpi]

    GOLD1 --> DASH1[Power BI Asset Risk Dashboard]
    GOLD2 --> DASH2[Operations SLA Dashboard]
    GOLD3 --> DASH3[Compliance Dashboard]
    GOLD1 --> API1[Client KPI API]
    GOLD3 --> API2[Client Compliance API]

    classDef fact fill:#E3F2FD,stroke:#1E88E5,stroke-width:2px,color:#0D47A1;
    classDef gold fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px,color:#4A148C;
    classDef cons fill:#FFF3E0,stroke:#FB8C00,stroke-width:2px,color:#E65100;
    class INSPECTION,INSPECTION_FINDING,WORK_ORDER,COMPLIANCE_RESULT fact;
    class GOLD1,GOLD2,GOLD3 gold;
    class DASH1,DASH2,DASH3,API1,API2 cons;
```

## 5) Interview Prep (Lead DE technical round)

Optional materials for SOCOTEC Data Engineer interview preparation:

| Path | Contents |
|------|----------|
| [`prep/interview-prep.md`](prep/interview-prep.md) | **All-in-one guide** — strategy, **§1.8 business**, **§1.9 friendly French**, cheatsheet, DE + business Q&A, mindmaps |
| [`src/interview_pyspark_example.py`](src/interview_pyspark_example.py) | Live-coding reference (aggregates + filters) |

Reported interview topic (Glassdoor, Dec 2025): **PySpark query with aggregates and filters** — see prep guide §2 Cheatsheet and example file.
