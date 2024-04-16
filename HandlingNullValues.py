import pandas as pd

# Assume df is a DataFrame that represents your supply chain data.
df = pd.read_csv('supply_chain_data.csv')

# Check the number of null values in each column.
print(df.isnull().sum())

# Fill null values with a specified value, for example, 0 or any other value that makes sense in your context.
df.fillna(0, inplace=True)

# Save the cleaned data to a new CSV file.
df.to_csv('cleaned_supply_chain_data.csv', index=False)

print(df)