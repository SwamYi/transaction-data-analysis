import pandas as pd

# Load the dataset
df = pd.read_csv("Bakery.csv")

# Check the structure of the data
print(df.info())

# Preview the first few rows
print(df.head())

# Check for duplicates based on specific columns
duplicate_rows = df[df.duplicated(subset=['TransactionNo', 'Items', 'DateTime'])]

# Print the number of duplicate rows
print(f"Number of duplicate rows: {duplicate_rows.shape[0]}")
# Optionally, preview the duplicates
print(duplicate_rows.head())

# Remove duplicates based on TransactionNo, Items, and DateTime
df = df.drop_duplicates(subset=['TransactionNo', 'Items', 'DateTime'], keep='first')

# Confirm the duplicates have been removed
print("all have been removed")

# Check for missing data in each column
missing_data = df.isnull().sum()
print(missing_data)


# Convert DateTime to pandas datetime format
df['DateTime'] = pd.to_datetime(df['DateTime'])

# Extract date (YYYY-MM-DD)
df['Date'] = df['DateTime'].dt.date

# Extract time (HH:MM:SS)
df['Time'] = df['DateTime'].dt.time

# Preview the updated dataframe
print(df[['DateTime', 'Date', 'Time']].head())

# Add DayType_fixed column (Day of the week)
df['DayType_fixed'] = df['DateTime'].dt.day_name()

# Extract the hour from the DateTime column
df['Hour'] = df['DateTime'].dt.hour

# Define Daypart categories
def categorize_daypart(hour):
    if 6 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 20:
        return 'Evening'
    else:
        return 'Night'

# Apply the function to create Daypart_fixed column
df['Daypart_fixed'] = df['Hour'].apply(categorize_daypart)

# Count the number of transactions for each item
item_sales = df['Items'].value_counts().reset_index()
item_sales.columns = ['Items', 'Total_Sales']

# Find the item(s) with the maximum sales
max_sales = item_sales['Total_Sales'].max()

# Get the list of popular items
popular_items = item_sales[item_sales['Total_Sales'] == max_sales]['Items'].tolist()

# Add the "Popular_Item" column
df['Popular_Item'] = df['Items'].apply(lambda x: 'Popular' if x in popular_items else 'Not Popular')

# Preview the updated dataframe
print(df[['Items', 'Popular_Item']].head())

# Save the dataset with the new "Popular_Item" column
df.to_csv("cleaned_data.csv", index=False)

