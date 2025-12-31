SELECT ch.chart_id,
       ch.tat_days,
       CASE
           WHEN tat_days <= 2 THEN 'Excellent'
           WHEN tat_days BETWEEN 3 AND 4 THEN 'Good'
           ELSE 'Needs Improvement'
       END AS performance
FROM charts ch;
