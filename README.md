Sales Data Engineering & Analytics Pipeline
Project Overview

This project demonstrates an end-to-end data engineering pipeline built using Python, PostgreSQL (Neon), and SQL.
It ingests raw transactional sales data from CSV files, transforms it into a star-schema data warehouse, and exposes business-ready KPI views for analytics and decision-making.

The project simulates a real-world retail analytics use case, focusing on scalability, data quality, and analytics readiness.

Architecture overview
Raw CSV Data
    │
    ▼
Python ETL (Pandas)
    │
    ├── Data Cleaning & Type Casting
    ├── Deduplication
    ├── Dimension Loading
    └── Fact Table Loading
    │
    ▼
PostgreSQL (Neon Cloud)
    │
    ├── Dimension Tables
    ├── Fact Table
    ├── KPI SQL Views
    └── Data Quality Checks

Tech Stack

Programming Language: Python

Database: PostgreSQL (Neon – Cloud Hosted)

Libraries: Pandas, psycopg2, python-dotenv

SQL Concepts:

Star Schema (Fact & Dimensions)

KPI Views

Data Quality Validation

Version Control: Git & GitHub

Project Structure
sales-data-pipeline-project/
│
├── data/
│   └── orders.csv
│
├── etl/
│   └── load_orders.py
│   └── test_connection.py
│
├── sql/
│   │
│   ├── create_raw_orders.sql
│   ├── schema/
│   │   ├── create_dim_tables.sql
│   │   └── create_fact_table.sql
│   │
│   ├── views/
│   │   ├── kpi_monthly_sales.sql
│   │   ├── kpi_top_profitable_products.sql
│   │   └── kpi_customer_segment_perf.sql
│   │
│   └── data_quality/
│       ├── duplicate_checks.sql
│       └── null_checks.sql
│
├── .env
├── README.md
└── .gitignore

Data Model (Star Schema)

Fact Table

fact_sales

order_id

customer_key

product_key

geography_key

order_date_key

sales

quantity

discount

profit

Dimension Tables

dim_customer (customer, segment)

dim_product (product, category, sub-category)

dim_geography (country, state, city, postal code)

dim_date (date, year, month, day)

ETL Workflow

Load raw CSV data using Pandas

Handle encoding issues (latin1)

Clean and normalize fields

Populate dimension tables with deduplication

Populate fact table with foreign keys

Validate data integrity

Expose analytics-ready KPI views

KPI SQL Views
1. Monthly Sales & Profit

Total orders

Total sales

Total profit

Profit margin %

2. Top Profitable Products

Identifies products contributing most to profit

3. Customer Segment Performance

Sales & profit by customer segment

These KPIs are implemented as PostgreSQL views to ensure a single source of truth for analytics.

Data Quality Checks

The project includes SQL-based validation for:

Duplicate records

NULL values in critical columns

This ensures analytical reliability and data trust.

Sample Results

Loaded 9,000+ transactional records

Created analytics-ready warehouse tables

Enabled fast KPI querying using SQL views