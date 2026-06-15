import sqlite3
import pandas as pd

conn = sqlite3.connect(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\01 - SaaS Churn Analysis\churn.db")

# ── QUERY 1: OVERALL CHURN RATE ──────────────────────────
print("=== Q1: OVERALL CHURN RATE ===")
q1 = pd.read_sql("""
    SELECT
        COUNT(*) AS total_customers,
        SUM(Churn) AS total_churned,
        ROUND(AVG(Churn) * 100, 1) AS churn_rate_pct
    FROM customers
""", conn)
print(q1)

# ── QUERY 2: CHURN & REVENUE AT RISK BY SUBSCRIPTION TYPE ─
print("\n=== Q2: CHURN & REVENUE AT RISK BY SUBSCRIPTION TYPE ===")
q2 = pd.read_sql("""
    SELECT
        [Subscription Type],
        COUNT(*) AS total_customers,
        SUM(Churn) AS churned,
        ROUND(AVG(Churn) * 100, 1) AS churn_rate_pct,
        ROUND(SUM(CASE WHEN Churn = 1 THEN [Total Spend] ELSE 0 END), 2) AS revenue_lost
    FROM customers
    GROUP BY [Subscription Type]
    ORDER BY churn_rate_pct DESC
""", conn)
print(q2)

# ── QUERY 3: CHURN BY CONTRACT LENGTH ────────────────────
print("\n=== Q3: CHURN BY CONTRACT LENGTH ===")
q3 = pd.read_sql("""
    SELECT
        [Contract Length],
        COUNT(*) AS total_customers,
        ROUND(AVG(Churn) * 100, 1) AS churn_rate_pct,
        ROUND(AVG([Total Spend]), 2) AS avg_spend
    FROM customers
    GROUP BY [Contract Length]
    ORDER BY churn_rate_pct DESC
""", conn)
print(q3)

# ── QUERY 4: HIGH RISK CUSTOMERS ─────────────────────────
# Monthly contract + 6+ support calls + churned
print("\n=== Q4: HIGH RISK PROFILE — MONTHLY + HIGH SUPPORT CALLS ===")
q4 = pd.read_sql("""
    SELECT
        [Contract Length],
        [Support Bucket],
        COUNT(*) AS total_customers,
        ROUND(AVG(Churn) * 100, 1) AS churn_rate_pct,
        ROUND(AVG([Total Spend]), 2) AS avg_spend
    FROM customers
    WHERE [Contract Length] = 'Monthly'
    GROUP BY [Support Bucket]
    ORDER BY churn_rate_pct DESC
""", conn)
print(q4)

# ── QUERY 5: REVENUE LOST TO CHURN BY CONTRACT TYPE ──────
print("\n=== Q5: TOTAL REVENUE LOST BY CONTRACT TYPE ===")
q5 = pd.read_sql("""
    SELECT
        [Contract Length],
        ROUND(SUM(CASE WHEN Churn = 1 THEN [Total Spend] ELSE 0 END), 2) AS revenue_lost,
        ROUND(SUM(CASE WHEN Churn = 0 THEN [Total Spend] ELSE 0 END), 2) AS revenue_retained
    FROM customers
    GROUP BY [Contract Length]
    ORDER BY revenue_lost DESC
""", conn)
print(q5)

# ── QUERY 6: CHURN BY TENURE BUCKET ──────────────────────
print("\n=== Q6: CHURN RATE BY TENURE ===")
q6 = pd.read_sql("""
    SELECT
        [Tenure Bucket],
        COUNT(*) AS total_customers,
        ROUND(AVG(Churn) * 100, 1) AS churn_rate_pct,
        ROUND(AVG([Total Spend]), 2) AS avg_spend
    FROM customers
    GROUP BY [Tenure Bucket]
    ORDER BY churn_rate_pct DESC
""", conn)
print(q6)

conn.close()
print("\nAll queries complete.")