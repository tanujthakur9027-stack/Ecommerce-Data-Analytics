import pandas as pd

# Load dataset
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

# Show first 5 rows
print(df.head())

# Show columns
print(df.columns)

# Convert dates
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

# Dataset info
print(df.info())

# Missing values
print(df.isnull().sum())

# Duplicate rows
print("Duplicates:", df.duplicated().sum())

# Dataset shape
print("Shape:", df.shape)
print(df.dtypes)
print(df['Sales'].sum())
print(df.groupby('Region')['Sales'].sum())
print(df.groupby('Category')['Profit'].sum())
print("Total Sales:", df['Sales'].sum())
print("Total Profit:", df['Profit'].sum())
print("Total Orders:", df['Order ID'].nunique())
print("Total Customers:", df['Customer ID'].nunique())

monthly_sales = df.groupby(
    df['Order Date'].dt.month
)['Sales'].sum()

print(monthly_sales)
yearly_sales = df.groupby(
    df['Order Date'].dt.year
)['Sales'].sum()

print(yearly_sales)

print(df.groupby('Region')['Sales'].sum())
print(df.groupby('Region')['Sales'].sum())
print(df.groupby('Category')['Sales'].sum())
print(df.groupby('Category')['Profit'].sum())
print(df.groupby('Sub-Category')['Sales'].sum())
print(
    df.groupby('Sub-Category')['Sales']
    .sum()
    .sort_values(ascending=False)
)
print(
    df.groupby('Customer Name')['Sales']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
print(
    df['Customer ID']
    .value_counts()
    .head(10)
)
print(
    df.groupby('Discount')['Profit']
    .mean()
)
import matplotlib.pyplot as plt

monthly_sales.plot(kind='bar')

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
category_sales = df.groupby('Category')['Sales'].sum()

category_sales.plot(kind='bar')

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.show()
df['Category'] = df['Category'].str.strip().str.title()

df['Sub-Category'] = df['Sub-Category'].str.strip().str.title()

df['Region'] = df['Region'].str.strip().str.title()
print(df[df['Sales'] < 0])
df = df[df['Sales'] >= 0]
df = df[df['Quantity'] > 0]
Q1 = df['Sales'].quantile(0.25)
Q3 = df['Sales'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print(lower, upper)
df = df[(df['Sales'] >= lower) & (df['Sales'] <= upper)]
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.month
df['Day'] = df['Order Date'].dt.day_name()
df['Delivery Days'] = (
    df['Ship Date'] - df['Order Date']
).dt.days
df.to_csv("cleaned_superstore.csv", index=False)
print(df.head())
print(df.info())

