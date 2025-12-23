CREATE OR REPLACE VIEW kpi_monthly_sales AS
SELECT
    d.year,
    d.month,
    COUNT(f.order_id) AS total_orders,
    SUM(f.sales) AS total_sales,
    SUM(f.profit) AS total_profit,
    ROUND(
        SUM(f.profit) / NULLIF(SUM(f.sales), 0) * 100,
        2
    ) AS profit_margin_pct
FROM fact_sales f
JOIN dim_date d
    ON f.order_date = d.date_id
GROUP BY d.year, d.month;

SELECT *
FROM kpi_monthly_sales
ORDER BY year, month;