import pandas as pd
import psycopg2
from psycopg2.extras import execute_batch
from dateutil import parser
from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "dbname": os.getenv("DB_NAME"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT")
}
# CSV_PATH = "../data/orders.csv"
# import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "..", "data", "orders.csv")

print("CSV exists:", os.path.exists(CSV_PATH))

# -----------------------------
# HELPERS
# -----------------------------
def parse_date(value):
    try:
        return parser.parse(str(value)).date()
    except Exception:
        return None

# -----------------------------
# MAIN ETL
# -----------------------------
def run_etl():
    print("Loading CSV...")
    df = pd.read_csv(CSV_PATH, encoding="latin1")

    # Rename columns to match SQL table
    df.columns = [
        "row_id", "order_id", "order_date", "ship_date", "ship_mode",
        "customer_id", "customer_name", "segment",
        "country", "city", "state", "postal_code", "region",
        "product_id", "category", "sub_category", "product_name",
        "sales", "quantity", "discount", "profit"
    ]

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Parse dates safely
    df["order_date_parsed"] = df["order_date"].apply(parse_date)
    df["ship_date_parsed"] = df["ship_date"].apply(parse_date)

    # Convert postal code to string
    df["postal_code"] = df["postal_code"].astype(str)

    # -----------------------------
    # CONNECT TO DB
    # -----------------------------
    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    # -----------------------------
    # LOAD RAW TABLE
    # -----------------------------
    print("Loading raw_orders...")
    raw_sql = """
        INSERT INTO raw_orders (
            row_id, order_id, order_date, ship_date, ship_mode,
            customer_id, customer_name, segment,
            country, city, state, postal_code, region,
            product_id, category, sub_category, product_name,
            sales, quantity, discount, profit
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    raw_data = [
        (
            r.row_id, r.order_id, r.order_date, r.ship_date, r.ship_mode,
            r.customer_id, r.customer_name, r.segment,
            r.country, r.city, r.state, r.postal_code, r.region,
            r.product_id, r.category, r.sub_category, r.product_name,
            r.sales, r.quantity, r.discount, r.profit
        )
        for r in df.itertuples(index=False)
    ]

    execute_batch(cur, raw_sql, raw_data)

    # -----------------------------
    # DIM CUSTOMER
    # -----------------------------
    print("Populating dim_customer...")
    cur.execute("""
        INSERT INTO dim_customer (customer_id, customer_name, segment)
        SELECT DISTINCT customer_id, customer_name, segment
        FROM raw_orders
        ON CONFLICT (customer_id) DO NOTHING;
    """)

    # -----------------------------
    # DIM PRODUCT
    # -----------------------------
    print("  Populating dim_product...")
    cur.execute("""
        INSERT INTO dim_product (product_id, product_name, category, sub_category)
        SELECT DISTINCT product_id, product_name, category, sub_category
        FROM raw_orders
        ON CONFLICT (product_id) DO NOTHING;
    """)

    # -----------------------------
    # DIM GEOGRAPHY
    # -----------------------------
    print("  Populating dim_geography...")
    cur.execute("""
        INSERT INTO dim_geography (country, city, state, postal_code, region)
        SELECT DISTINCT country, city, state, postal_code, region
        FROM raw_orders
        WHERE (country, city, state, postal_code, region)
        NOT IN (
            SELECT country, city, state, postal_code, region FROM dim_geography
        );
    """)

    # -----------------------------
    # DIM DATE
    # -----------------------------
    print("Populating dim_date...")
    all_dates = pd.concat([
        df["order_date_parsed"],
        df["ship_date_parsed"]
    ]).dropna().unique()

    date_sql = """
        INSERT INTO dim_date (date_id, year, month, day)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (date_id) DO NOTHING;
    """

    date_rows = [(d, d.year, d.month, d.day) for d in all_dates]
    execute_batch(cur, date_sql, date_rows)

    # -----------------------------
    # FACT SALES
    # -----------------------------
    print("Populating fact_sales...")
    cur.execute("""
        INSERT INTO fact_sales (
            order_id, order_date, ship_date,
            customer_id, product_id, geo_id,
            sales, quantity, discount, profit
        )
        SELECT
            r.order_id,
            CAST(r.order_date AS DATE),
            CAST(r.ship_date AS DATE),
            r.customer_id,
            r.product_id,
            g.geo_id,
            r.sales,
            r.quantity,
            r.discount,
            r.profit
        FROM raw_orders r
        JOIN dim_geography g
          ON r.country = g.country
         AND r.city = g.city
         AND r.state = g.state
         AND r.postal_code = g.postal_code
         AND r.region = g.region;
    """)

    conn.commit()
    cur.close()
    conn.close()

    print("ETL COMPLETED SUCCESSFULLY")

# -----------------------------
if __name__ == "__main__":
    run_etl()
