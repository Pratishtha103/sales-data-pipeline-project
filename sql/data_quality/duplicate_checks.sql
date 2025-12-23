-- Duplicate Order IDs in fact table
SELECT
    order_id,
    COUNT(*) AS duplicate_count
FROM fact_sales
GROUP BY order_id
HAVING COUNT(*) > 1;


-- Duplicate customers (same customer_id)
SELECT
    customer_id,
    COUNT(*) AS duplicate_count
FROM dim_customer
GROUP BY customer_id
HAVING COUNT(*) > 1;


-- Duplicate products (same product_id)
SELECT
    product_id,
    COUNT(*) AS duplicate_count
FROM dim_product
GROUP BY product_id
HAVING COUNT(*) > 1;


-- Duplicate geography entries
SELECT
    country,
    state,
    city,
    postal_code,
    COUNT(*) AS duplicate_count
FROM dim_geography
GROUP BY country, state, city, postal_code
HAVING COUNT(*) > 1;
