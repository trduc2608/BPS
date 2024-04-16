import pandas as pd

# Load the supply chain data into a DataFrame.
df = pd.read_csv('supply_chain_data.csv')

# Create a dictionary mapping the current column names to the desired column names.
column_mapping = {
    'ProductName': 'Product Name',
    'SupplierID': 'ID',
    'Quantity': 'Quantity (units)',
    'UnitCost': 'Unit Price',
    'InventoryLevel': 'Inventory Level',
    'OrderStatus': 'Status'
}

# Rename the columns using the mapping dictionary.
df.rename(columns=column_mapping, inplace=True)

# Save the modified DataFrame to a new CSV file.
df.to_csv('renamed_supply_chain_data.csv', index=False)

print(df)