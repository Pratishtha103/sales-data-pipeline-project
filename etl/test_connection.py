import psycopg2
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=os.getenv("DB_PORT"),
    sslmode="require"
)

print("✅ Connected to Neon PostgreSQL successfully!")
conn.close()
