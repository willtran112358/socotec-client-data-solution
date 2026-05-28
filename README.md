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

### 1.4 Business Visuals (Mermaid)
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
    subgraph S1[Data Sources]
        ERP[ERP and Finance]
        CRM[CRM and Sales]
        IOT[IoT Sensors]
        APP[Inspection Apps]
        EXT[External Data]
    end

    subgraph S2[Ingestion]
        CDC[CDC Connectors]
        BATCH[Batch ELT Jobs]
        STREAM[Kafka Streams]
    end

    subgraph S3[Lakehouse]
        BRONZE[Bronze Raw Delta]
        SILVER[Silver Curated Delta]
        GOLD[Gold Business Marts]
    end

    subgraph S4[Consumption]
        BI[BI Dashboards]
        API[Client APIs]
        GENAI[GenAI Assistant]
    end

    ERP --> CDC
    CRM --> CDC
    IOT --> STREAM
    APP --> BATCH
    EXT --> BATCH
    CDC --> BRONZE
    BATCH --> BRONZE
    STREAM --> BRONZE
    BRONZE --> SILVER --> GOLD
    GOLD --> BI
    GOLD --> API
    GOLD --> GENAI

    classDef src fill:#EDE7F6,stroke:#5E35B1,stroke-width:2px,color:#311B92;
    classDef ing fill:#E1F5FE,stroke:#039BE5,stroke-width:2px,color:#01579B;
    classDef med fill:#F3E5F5,stroke:#8E24AA,stroke-width:2px,color:#4A148C;
    classDef con fill:#FFF8E1,stroke:#F9A825,stroke-width:2px,color:#F57F17;
    class ERP,CRM,IOT,APP,EXT src;
    class CDC,BATCH,STREAM ing;
    class BRONZE,SILVER,GOLD med;
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
    subgraph SILVER_FLOW["Function silver_inspections"]
        B1["Read stream bronze_inspections"] --> B2["Expectation asset_id not null"]
        B2 --> B3["Expectation inspection_date not null"]
        B3 --> B4["Create hashed inspector_key"]
        B4 --> B5["Drop inspector_email column"]
        B5 --> B6["Add updated_at timestamp"]
        B6 --> B7["Output DLT table silver_inspections"]
    end

    subgraph GOLD_FLOW["Function gold_asset_risk_kpi"]
        G1["Read DLT table silver_inspections"] --> G3["Inner join on asset_id"]
        G2["Read table silver_assets"] --> G3
        G3 --> G4["Group by client and asset"]
        G4 --> G5["Aggregate inspection_id count"]
        G5 --> G6["Aggregate non_conformity_score average"]
        G6 --> G7["Rename final KPI columns"]
        G7 --> G8["Output DLT table gold_asset_risk_kpi"]
    end

    classDef silver fill:#EDE7F6,stroke:#5E35B1,stroke-width:2px,color:#311B92;
    classDef gold fill:#FFF8E1,stroke:#F9A825,stroke-width:2px,color:#F57F17;
    class B1,B2,B3,B4,B5,B6,B7 silver;
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

    M --> M1["product_name"]
    M --> M2["version"]
    M --> M3["owner_team"]

    S --> S1["refresh_frequency: daily"]
    S --> S2["availability: 99.5%"]

    F --> F1["client_id: string"]
    F --> F2["asset_id: string"]
    F --> F3["criticality_level: string"]
    F --> F4["inspection_count: long"]
    F --> F5["avg_non_conformity_score: double"]
    F --> F6["updated_at: timestamp"]

    SEC --> SC1["contains_pii: false"]
    SEC --> SC2["access_policy: rbac_client_scope"]

    classDef root fill:#E8EAF6,stroke:#3949AB,stroke-width:2px,color:#1A237E;
    classDef group fill:#E0F7FA,stroke:#00838F,stroke-width:2px,color:#004D40;
    classDef leaf fill:#FFF3E0,stroke:#EF6C00,stroke-width:2px,color:#E65100;
    class ROOT root;
    class M,S,F,SEC group;
    class M1,M2,M3,S1,S2,F1,F2,F3,F4,F5,F6,SC1,SC2 leaf;
```
