import pandas as pd

# Load the supply chain data into a DataFrame.
df = pd.read_csv('supply_chain_data.csv')

# Check the number of empty rows in the DataFrame.
print(f"Number of empty rows before cleaning: {df.isnull().sum().sum()}")

# Remove empty rows from the DataFrame.
df.dropna(how='any', inplace=True)

# Verify that the empty rows have been removed.
print(f"Number of empty rows after cleaning: {df.isnull().sum().sum()}")

# Save the cleaned data to a new CSV file.
df.to_csv('cleaned_supply_chain_data.csv', index=False)

print(df)