import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\01 - SaaS Churn Analysis\churn.db")

# Pull everything we need for the dashboard
df = pd.read_sql("""
    SELECT
        Age,
        Gender,
        Tenure,
        [Usage Frequency],
        [Support Calls],
        [Payment Delay],
        [Subscription Type],
        [Contract Length],
        [Total Spend],
        [Last Interaction],
        Churn,
        [Tenure Bucket],
        [Support Bucket],
        CASE WHEN Churn = 1 THEN 'Churned' ELSE 'Retained' END AS Churn_Label,
        CASE WHEN Churn = 1 THEN [Total Spend] ELSE 0 END AS Revenue_Lost,
        CASE WHEN Churn = 0 THEN [Total Spend] ELSE 0 END AS Revenue_Retained
    FROM customers
""", conn)

# Export
df.to_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\01 - SaaS Churn Analysis\csv\churn_tableau.csv", index=False)
print(f"Tableau export complete. Rows: {len(df)}")
conn.close()