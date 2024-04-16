import pandas as pd

# Load the supply chain data into a DataFrame.
df = pd.read_csv('supply_chain_data.csv')

print(df)

# Check the number of duplicate entries in the DataFrame.
print(f"Number of duplicate entries before cleaning: {df.duplicated().sum()}")

# Remove duplicate entries from the DataFrame.
df.drop_duplicates(inplace=True)

# Verify that the duplicate entries have been removed.
print(f"Number of duplicate entries after cleaning: {df.duplicated().sum()}")

# Save the cleaned data to a new CSV file.
df.to_csv('cleaned_supply_chain_data.csv', index=False)

print(df)