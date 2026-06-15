import pandas as pd
import sqlite3

# Load the analyzed CSV
df = pd.read_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\01 - SaaS Churn Analysis\csv\churn_analyzed.csv")

# Create (or connect to) a SQLite database in your project folder
conn = sqlite3.connect(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\01 - SaaS Churn Analysis\churn.db")

# Load the dataframe into a table called 'customers'
df.to_sql('customers', conn, if_exists='replace', index=False)

print("Database created and table loaded.")
print(f"Rows loaded: {len(df)}")

# Quick sanity check — pull first 5 rows straight from SQL
check = pd.read_sql("SELECT * FROM customers LIMIT 5", conn)
print("\n=== FIRST 5 ROWS FROM SQL ===")
print(check)

conn.close()