-- NULL checks in fact_sales
SELECT
    COUNT(*) FILTER (WHERE order_id IS NULL)        AS null_order_id,
    COUNT(*) FILTER (WHERE customer_id IS NULL)   AS null_customer_key,
    COUNT(*) FILTER (WHERE product_id IS NULL)    AS null_product_key,
    COUNT(*) FILTER (WHERE order_date IS NULL) AS null_date_key,
    COUNT(*) FILTER (WHERE sales IS NULL)           AS null_sales,
    COUNT(*) FILTER (WHERE profit IS NULL)          AS null_profit
FROM fact_sales;


-- Negative or invalid sales/profit
SELECT
    COUNT(*) FILTER (WHERE sales < 0)  AS negative_sales,
    COUNT(*) FILTER (WHERE profit < 0) AS negative_profit
FROM fact_sales;


-- NULL checks in dim_customer
SELECT
    COUNT(*) FILTER (WHERE customer_id IS NULL) AS null_customer_id,
    COUNT(*) FILTER (WHERE customer_name IS NULL) AS null_customer_name,
    COUNT(*) FILTER (WHERE segment IS NULL) AS null_segment
FROM dim_customer;


-- NULL checks in dim_product
SELECT
    COUNT(*) FILTER (WHERE product_id IS NULL) AS null_product_id,
    COUNT(*) FILTER (WHERE product_name IS NULL) AS null_product_name,
    COUNT(*) FILTER (WHERE category IS NULL) AS null_category
FROM dim_product;


-- NULL checks in dim_date
SELECT
    COUNT(*) FILTER (WHERE date_id IS NULL) AS null_date,
    COUNT(*) FILTER (WHERE year IS NULL) AS null_year,
    COUNT(*) FILTER (WHERE month IS NULL) AS null_month
FROM dim_date;