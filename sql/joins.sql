-- LEFT JOIN example

SELECT co.coder_name, ch.chart_id
FROM coders co
LEFT JOIN charts ch
ON co.coder_id = ch.coder_id;
