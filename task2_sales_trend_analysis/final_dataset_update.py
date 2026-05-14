import pandas as pd

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv(
    r"C:\Users\Tanuj kumar singh\Downloads\Ecommerce_Project\cleaned_data\data.csv",
    encoding='latin1'
)

# =====================================================
# CONVERT DATE
# =====================================================

df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    errors='coerce'
)

# =====================================================
# CREATE NEW COLUMNS
# =====================================================

df['Year'] = df['Order Date'].dt.year

df['Month'] = df['Order Date'].dt.month_name()

# =====================================================
# REGION SALES
# =====================================================

region_sales = df.groupby('Region')['Sales'].transform('sum')

df['Region Total Sales'] = region_sales

# =====================================================
# CATEGORY SALES
# =====================================================

category_sales = df.groupby('Category')['Sales'].transform('sum')

df['Category Total Sales'] = category_sales

# =====================================================
# SAVE UPDATED DATASET
# =====================================================

df.to_csv(
    "updated_sales_analysis_dataset.csv",
    index=False
)

print("Updated Dataset Saved Successfully!")