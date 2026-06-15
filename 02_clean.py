import pandas as pd

# Load and combine
train = pd.read_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\01 - SaaS Churn Analysis\csv\customer_churn_dataset-training-master.csv")
test = pd.read_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\01 - SaaS Churn Analysis\csv\customer_churn_dataset-testing-master.csv")
df = pd.concat([train, test], ignore_index=True)

# ── CLEANING ────────────────────────────────────────────

# Drop the one fully blank row
df = df.dropna()
print(f"Rows after dropping nulls: {len(df)}")

# Churn column is 1.0/0.0 floats — convert to clean integers
df['Churn'] = df['Churn'].astype(int)

# CustomerID isn't needed for analysis — drop it
df = df.drop(columns=['CustomerID'])

# Confirm everything looks right
print("\n=== CLEANED DATA TYPES ===")
print(df.dtypes)

print("\n=== FINAL SHAPE ===")
print(df.shape)

print("\n=== QUICK STATS ===")
print(df.describe())

# Save cleaned file for use in next steps
df.to_csv(r"C:\Users\bryce\Desktop\Data Projects\Side Projects\SaaS Practice\01 - SaaS Churn Analysis\csv\churn_cleaned.csv", index=False)
print("\nCleaned file saved.")