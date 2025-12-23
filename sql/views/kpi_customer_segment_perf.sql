CREATE OR REPLACE VIEW kpi_customer_segment_perf AS
SELECT
    c.segment,
    COUNT(DISTINCT f.customer_id) AS total_customers,
    SUM(f.sales)                   AS total_sales,
    SUM(f.profit)                  AS total_profit
FROM fact_sales f
JOIN dim_customer c
    ON f.customer_id = c.customer_id
GROUP BY c.segment;

SELECT *
FROM kpi_customer_segment_perf 
ORDER BY total_profit DESC;