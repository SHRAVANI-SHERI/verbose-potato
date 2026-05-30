import pandas as pd

# Read CSV file
df = pd.read_csv('../data/raw_data.csv')

print("Original Data")
print(df)

# Remove duplicates
df = df.drop_duplicates()

# Fill missing names
df['name'] = df['name'].fillna("Unknown")

# Convert dates
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Standard date format
df['date'] = df['date'].dt.strftime('%Y-%m-%d')

# Save cleaned file
df.to_csv('../data/cleaned_data.csv', index=False)

print("\nCleaned Data")
print(df)

print("\nProject Completed Successfully")