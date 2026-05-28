-- Example quality checks for Gold data products

-- 1) Freshness check
SELECT
  CASE WHEN MAX(updated_at) >= current_timestamp() - INTERVAL 1 DAY THEN 'PASS' ELSE 'FAIL' END AS freshness_status
FROM gold_asset_risk_kpi;

-- 2) Null check on key business dimensions
SELECT
  COUNT(*) AS null_key_rows
FROM gold_asset_risk_kpi
WHERE client_id IS NULL OR asset_id IS NULL;

-- 3) Threshold check: non conformity score range
SELECT
  COUNT(*) AS out_of_range_rows
FROM gold_asset_risk_kpi
WHERE avg_non_conformity_score < 0 OR avg_non_conformity_score > 100;
