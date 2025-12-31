-- Healthcare Productivity & SLA Analysis

-- Simulated table: charts

-- 1. Productivity by coder
SELECT
    coder_name,
    COUNT(chart_id) AS charts_completed
FROM charts
GROUP BY coder_name
ORDER BY charts_completed DESC;


-- 2. SLA performance classification
SELECT
    chart_id,
    coder_name,
    tat_days,
    CASE
        WHEN tat_days <= 2 THEN 'Excellent'
        WHEN tat_days BETWEEN 3 AND 4 THEN 'Good'
        ELSE 'Needs Improvement'
    END AS performance
FROM charts;


-- 3. SLA breach analysis
SELECT
    chart_id,
    coder_name,
    tat_days
FROM charts
WHERE tat_days > 4
ORDER BY tat_days DESC;
