import pandas as pd

# Load the supply chain data into a DataFrame.
df = pd.read_csv('supply_chain_data.csv')

# Replace incorrect product codes
df.replace({'ProductName': {'WidgetA': 'WidgetX', 'WidgetB': 'WidgetY'}}, inplace=True)

# Replace incorrect pricing
df['UnitCost'] = df['UnitCost'].replace(0, 10.00)

# Replace inconsistent inventory levels
df.fillna({'InventoryLevel' : 0}, inplace=True)
df.fillna({'Quantity' : 0}, inplace=True)

# Save the cleaned data to a new CSV file.
df.to_csv('cleaned_supply_chain_data.csv', index=False)

print(df)