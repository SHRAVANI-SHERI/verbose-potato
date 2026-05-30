import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('../data/customers.csv')

print("Customer Dataset")
print(df)

# -----------------------------
# Churn Summary
# -----------------------------
print("\nChurn Summary")
print(df['Churn'].value_counts())

# -----------------------------
# Average Monthly Charges
# -----------------------------
print("\nAverage Monthly Charges")
print(df.groupby('Churn')['MonthlyCharges'].mean())

# -----------------------------
# Average Support Calls
# -----------------------------
print("\nAverage Support Calls")
print(df.groupby('Churn')['SupportCalls'].mean())

# -----------------------------
# Create Bar Chart
# -----------------------------
df['Churn'].value_counts().plot(kind='bar')

plt.title("Customer Churn Analysis")
plt.xlabel("Churn")
plt.ylabel("Count")

plt.show()

# -----------------------------
# Insights
# -----------------------------
print("\nInsights:")
print("Customers with low usage and high support calls are more likely to churn.")

print("\nSuggestions:")
print("Improve customer support and customer engagement.")