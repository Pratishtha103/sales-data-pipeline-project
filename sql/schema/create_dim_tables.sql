-- DIM CUSTOMER
CREATE TABLE dim_customer (
    customer_id TEXT PRIMARY KEY,
    customer_name TEXT,
    segment TEXT
);

-- DIM PRODUCT
CREATE TABLE dim_product (
    product_id TEXT PRIMARY KEY,
    product_name TEXT,
    category TEXT,
    sub_category TEXT
);

-- DIM GEOGRAPHY
CREATE TABLE dim_geography (
    geo_id SERIAL PRIMARY KEY,
    country TEXT,
    city TEXT,
    state TEXT,
    postal_code TEXT,
    region TEXT
);

-- DIM DATE
CREATE TABLE dim_date (
    date_id DATE PRIMARY KEY,
    year INTEGER,
    month INTEGER,
    day INTEGER
);

SELECT COUNT(*) FROM dim_customer;
SELECT COUNT(*) FROM dim_product;
SELECT COUNT(*) FROM dim_geography;
SELECT COUNT(*) FROM dim_date;