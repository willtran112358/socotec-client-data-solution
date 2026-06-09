-- Monitoring data quality checks — project-scoped, aligned with VN intern JD
-- Validates: equipment health, reading completeness, anomaly integrity, report freshness

-- 1) Sensor freshness: no reading in last 2 hours → FAIL for 24/7 monitoring SLA
SELECT
  project_id,
  sensor_id,
  MAX(reading_ts) AS last_reading_at,
  CASE
    WHEN MAX(reading_ts) >= current_timestamp() - INTERVAL 2 HOUR THEN 'PASS'
    ELSE 'FAIL'
  END AS freshness_status
FROM silver_sensor_readings
GROUP BY project_id, sensor_id
HAVING freshness_status = 'FAIL';

-- 2) Equipment health: offline sensors block report sign-off
SELECT
  project_id,
  COUNT(*) AS offline_sensor_count
FROM gold_sensor_health_kpi
WHERE health_status = 'OFFLINE'
GROUP BY project_id
HAVING offline_sensor_count > 0;

-- 3) Reading completeness: gap detection (expected interval vs actual)
SELECT
  project_id,
  sensor_id,
  COUNT(*) AS reading_count,
  MIN(reading_ts) AS period_start,
  MAX(reading_ts) AS period_end
FROM silver_sensor_readings
WHERE reading_ts >= current_timestamp() - INTERVAL 1 DAY
GROUP BY project_id, sensor_id
HAVING reading_count < 24;  -- example: hourly sampling expects >= 24 readings/day

-- 4) Threshold config integrity: every active sensor must have a valid config
SELECT
  s.sensor_id,
  s.project_id
FROM silver_sensors s
LEFT JOIN silver_sensor_config c ON s.sensor_id = c.sensor_id
WHERE s.deployment_status = 'ACTIVE'
  AND (c.sensor_id IS NULL OR c.threshold_min IS NULL OR c.threshold_max IS NULL);

-- 5) Anomaly KPI range: negative counts are invalid
SELECT COUNT(*) AS invalid_anomaly_rows
FROM gold_sensor_anomaly_kpi
WHERE anomaly_count < 0;

-- 6) Periodic report freshness by cadence
SELECT
  report_period,
  project_id,
  CASE
    WHEN report_period = 'daily' AND MAX(published_at) >= current_timestamp() - INTERVAL 1 DAY THEN 'PASS'
    WHEN report_period = 'weekly' AND MAX(published_at) >= current_timestamp() - INTERVAL 7 DAY THEN 'PASS'
    WHEN report_period = 'monthly' AND MAX(published_at) >= current_timestamp() - INTERVAL 31 DAY THEN 'PASS'
    ELSE 'FAIL'
  END AS report_freshness_status
FROM (
  SELECT project_id, 'daily' AS report_period, published_at FROM gold_monitoring_report_daily
  UNION ALL
  SELECT project_id, 'weekly' AS report_period, published_at FROM gold_monitoring_report_weekly
  UNION ALL
  SELECT project_id, 'monthly' AS report_period, published_at FROM gold_monitoring_report_monthly
)
GROUP BY report_period, project_id
HAVING report_freshness_status = 'FAIL';
