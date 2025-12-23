-- FACT TABLE
CREATE TABLE fact_sales (
    order_id TEXT,
    order_date DATE,
    ship_date DATE,
    customer_id TEXT,
    product_id TEXT,
    geo_id INTEGER,
    sales NUMERIC(10,4),
    quantity INTEGER,
    discount NUMERIC(4,2),
    profit NUMERIC(10,4),
    FOREIGN KEY (customer_id) REFERENCES dim_customer(customer_id),
    FOREIGN KEY (product_id) REFERENCES dim_product(product_id),
    FOREIGN KEY (geo_id) REFERENCES dim_geography(geo_id)
);

SELECT COUNT(*) FROM fact_sales;