CREATE OR REPLACE VIEW kpi_top_profitable_products AS
SELECT
    p.product_name,
    p.category,
    SUM(f.sales)  AS total_sales,
    SUM(f.profit) AS total_profit
FROM fact_sales f
JOIN dim_product p
    ON f.product_id = p.product_id
GROUP BY p.product_name, p.category
LIMIT 10;

SELECT *
FROM kpi_top_profitable_products
ORDER BY total_profit DESC;