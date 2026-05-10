# =========================================================
# TASK 2: DOWNLOAD AND EXPLORE E-COMMERCE DATASET
# Complete Code Covering All Subtasks
# =========================================================

# STEP 1 — Import Libraries
import pandas as pd

# =========================================================
# STEP 2 — Load Dataset
# =========================================================

# Replace file name if your CSV name is different
df = pd.read_csv("Sample - Superstore.csv", encoding='latin1')

print("Dataset Loaded Successfully!\n")

# =========================================================
# STEP 3 — Display First Few Rows
# =========================================================

print("FIRST 5 ROWS OF DATASET")
print(df.head())

# =========================================================
# STEP 4 — Explore Dataset Structure
# =========================================================

# Dataset Shape
print("\nDATASET SHAPE")
print(df.shape)

# Rows and Columns separately
print("\nTOTAL ROWS:", df.shape[0])
print("TOTAL COLUMNS:", df.shape[1])

# Column Names
print("\nCOLUMN NAMES")
print(df.columns)

# Data Types
print("\nDATA TYPES")
print(df.dtypes)

# Dataset Information
print("\nDATASET INFORMATION")
print(df.info())

# =========================================================
# STEP 5 — Check Important Columns
# =========================================================

print("\nIMPORTANT COLUMNS CHECK")

important_columns = [
    'Order ID',
    'Order Date',
    'Customer ID',
    'Sales',
    'Quantity',
    'Profit',
    'Category',
    'Region'
]

for col in important_columns:
    if col in df.columns:
        print(f"{col} → Present")
    else:
        print(f"{col} → Not Present")

# =========================================================
# STEP 6 — Identify Missing Values
# =========================================================

print("\nMISSING VALUES")
print(df.isnull().sum())

# Total Missing Values
print("\nTOTAL MISSING VALUES:")
print(df.isnull().sum().sum())

# =========================================================
# STEP 7 — Identify Duplicate Records
# =========================================================

print("\nDUPLICATE RECORDS")
duplicates = df.duplicated().sum()

print("Total Duplicate Rows:", duplicates)

# =========================================================
# STEP 8 — Convert Date Columns
# =========================================================

print("\nCONVERTING DATE COLUMNS")

df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    errors='coerce'
)

df['Ship Date'] = pd.to_datetime(
    df['Ship Date'],
    errors='coerce'
)

print("Date Conversion Completed!")

# Check Data Types Again
print("\nUPDATED DATA TYPES")
print(df.dtypes)

# =========================================================
# STEP 9 — Basic Statistical Summary
# =========================================================

print("\nSTATISTICAL SUMMARY")
print(df.describe())

# =========================================================
# STEP 10 — Identify Key Columns for Analysis
# =========================================================

print("\nKEY COLUMNS FOR ANALYSIS")

# Sales Columns
sales_columns = ['Sales', 'Profit', 'Quantity', 'Discount']

# Customer Columns
customer_columns = ['Customer ID', 'Customer Name', 'Segment']

# Product Columns
product_columns = ['Category', 'Sub-Category', 'Product Name']

# Geographic Columns
geo_columns = ['Country', 'City', 'State', 'Region']

print("\nSales Related Columns:")
print(sales_columns)

print("\nCustomer Related Columns:")
print(customer_columns)

print("\nProduct Related Columns:")
print(product_columns)

print("\nGeographic Columns:")
print(geo_columns)

# =========================================================
# STEP 11 — Sample Exploratory Analysis
# =========================================================

# Total Sales
print("\nTOTAL SALES")
print(df['Sales'].sum())

# Total Profit
print("\nTOTAL PROFIT")
print(df['Profit'].sum())

# Sales by Category
print("\nSALES BY CATEGORY")
print(df.groupby('Category')['Sales'].sum())

# Profit by Region
print("\nPROFIT BY REGION")
print(df.groupby('Region')['Profit'].sum())

# =========================================================
# STEP 12 — Save Explored Dataset
# =========================================================

df.to_csv("explored_superstore.csv", index=False)

print("\nDATASET SAVED SUCCESSFULLY!")
print("File Name: explored_superstore.csv")

# =========================================================
# STEP 13 — Final Observations
# =========================================================

print("\nFINAL OBSERVATIONS")

print("""
1. Dataset successfully loaded and explored.
2. Dataset contains sales, customer, product, and regional data.
3. Date columns converted into datetime format.
4. Missing values and duplicate records identified.
5. Dataset ready for data cleaning and preprocessing.
6. Key business metrics identified for analysis.
""")

