import pandas as pd

# Load the cleaned file
df = pd.read_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\01 - SaaS Churn Analysis\csv\churn_cleaned.csv")

# ── OVERALL CHURN RATE ───────────────────────────────────
overall_churn = df['Churn'].mean() * 100
print(f"=== OVERALL CHURN RATE ===")
print(f"{overall_churn:.1f}%")

# ── CHURN BY SUBSCRIPTION TYPE ───────────────────────────
print("\n=== CHURN RATE BY SUBSCRIPTION TYPE ===")
churn_by_sub = df.groupby('Subscription Type')['Churn'].mean() * 100
print(churn_by_sub.round(1))

# ── CHURN BY CONTRACT LENGTH ─────────────────────────────
print("\n=== CHURN RATE BY CONTRACT LENGTH ===")
churn_by_contract = df.groupby('Contract Length')['Churn'].mean() * 100
print(churn_by_contract.round(1))

# ── CHURN BY TENURE BUCKET ───────────────────────────────
# Group customers into how long they've been around
df['Tenure Bucket'] = pd.cut(
    df['Tenure'],
    bins=[0, 6, 12, 24, 36, 60],
    labels=['0-6 mo', '7-12 mo', '13-24 mo', '25-36 mo', '37-60 mo']
)
print("\n=== CHURN RATE BY TENURE ===")
churn_by_tenure = df.groupby('Tenure Bucket', observed=True)['Churn'].mean() * 100
print(churn_by_tenure.round(1))

# ── CHURN BY SUPPORT CALLS BUCKET ────────────────────────
df['Support Bucket'] = pd.cut(
    df['Support Calls'],
    bins=[-1, 1, 3, 5, 10],
    labels=['0-1 calls', '2-3 calls', '4-5 calls', '6+ calls']
)
print("\n=== CHURN RATE BY SUPPORT CALLS ===")
churn_by_support = df.groupby('Support Bucket', observed=True)['Churn'].mean() * 100
print(churn_by_support.round(1))

# ── AVERAGE SPEND: CHURNED VS STAYED ─────────────────────
print("\n=== AVG TOTAL SPEND: CHURNED VS STAYED ===")
spend_comparison = df.groupby('Churn')['Total Spend'].mean().round(2)
spend_comparison.index = ['Stayed', 'Churned']
print(spend_comparison)

# Save for use in dashboard later
df.to_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\01 - SaaS Churn Analysis\csv\churn_analyzed.csv", index=False)
print("\nAnalyzed file saved.")