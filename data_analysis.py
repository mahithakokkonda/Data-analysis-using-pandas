import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "C:/Users/MAHITHA/OneDrive/Desktop/mahitha/Blackpearl internship/sample_sales_data.csv"  # Update this to the correct path
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(data.head())

# Filter data for the 'north' region
north_region_sales = data[data['Region'] == 'north']

# Sort data by 'sales_amount' in descending order
sorted_sales = data.sort_values(by='sales_amount', ascending=False)

# Group data by 'Region' and calculate aggregated statistics
grouped_by_region = data.groupby('Region').agg({
    'sales_amount': ['mean', 'median', 'std'],
    'units_sold': ['mean', 'median', 'std']
}).reset_index()

print("\nFiltered Data for 'North' Region:")
print(north_region_sales.head())

print("\nSorted Data by 'sales_amount' (Top 5 Records):")
print(sorted_sales.head())

print("\nGrouped Data by 'Region' with Aggregated Statistics:")
print(grouped_by_region)

# Calculate summary statistics for the entire dataset
summary_stats = data.describe()
print("\nSummary Statistics for Numeric Variables:")
print(summary_stats)

# Visualize data distributions and relationships
# Histogram for the distribution of 'sales_amount'
plt.figure(figsize=(10, 6))
sns.histplot(data['sales_amount'], kde=True)
plt.title('Distribution of Sales Amount')
plt.xlabel('Sales Amount')
plt.ylabel('Frequency')
plt.show()

# Box plot for 'sales_amount' by 'Region'
plt.figure(figsize=(10, 6))
sns.boxplot(x='Region', y='sales_amount', data=data)
plt.title('Sales Amount by Region')
plt.xlabel('Region')
plt.ylabel('Sales Amount')
plt.show()

# Scatter plot to show the relationship between 'sales_amount' and 'units_sold'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sales_amount', y='units_sold', hue='Region', data=data)
plt.title('Sales Amount vs Units Sold')
plt.xlabel('Sales Amount')
plt.ylabel('Units Sold')
plt.show()
