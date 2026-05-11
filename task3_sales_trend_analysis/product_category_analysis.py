import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Users\Tanuj kumar singh\Downloads\Ecommerce_Project\cleaned_data\data.csv",
    encoding='latin1'
)

print(df.head())

# =====================================================
# TOP PRODUCTS ANALYSIS
# =====================================================

product_sales = df.groupby('Product Name').agg({
    'Sales': 'sum',
    'Quantity': 'sum',
    'Profit': 'sum'
})

# Sort by highest sales
top_products = product_sales.sort_values(
    by='Sales',
    ascending=False
)

# Top 10 Products
top_10_products = top_products.head(10)

print("\nTOP 10 PRODUCTS")
print(top_10_products)

# =====================================================
# CATEGORY ANALYSIS
# =====================================================

category_sales = df.groupby('Category').agg({
    'Sales': 'sum',
    'Quantity': 'sum',
    'Profit': 'sum'
})

# Sort categories by sales
category_sales = category_sales.sort_values(
    by='Sales',
    ascending=False
)

print("\nCATEGORY ANALYSIS")
print(category_sales)

# =====================================================
# TOP 10 PRODUCTS BAR CHART
# =====================================================

plt.figure(figsize=(12,6))

top_10_products['Sales'].plot(
    kind='bar'
)

plt.title("Top 10 Best-Selling Products")

plt.xlabel("Product Name")

plt.ylabel("Total Sales")

plt.xticks(rotation=75)

plt.tight_layout()

plt.savefig("top_10_products.png")

plt.show()

# =====================================================
# CATEGORY SALES PIE CHART
# =====================================================

plt.figure(figsize=(8,8))

category_sales['Sales'].plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Sales Contribution by Category")

plt.ylabel("")

plt.tight_layout()

plt.savefig("category_sales_pie.png")

plt.show()

# =====================================================
# TOP PROFITABLE PRODUCTS
# =====================================================

top_profit_products = df.groupby(
    'Product Name'
).agg({
    'Profit': 'sum',
    'Sales': 'sum'
})

# Sort by profit
top_profit_products = top_profit_products.sort_values(
    by='Profit',
    ascending=False
)

# Top 10 profitable products
top_10_profit_products = top_profit_products.head(10)

print("\nTOP 10 PROFITABLE PRODUCTS")
print(top_10_profit_products)

# =====================================================
# TOP PROFITABLE PRODUCTS CHART
# =====================================================

plt.figure(figsize=(12,6))

top_10_profit_products['Profit'].plot(
    kind='bar',
    color='green'
)

plt.title("Top 10 Most Profitable Products")

plt.xlabel("Product Name")

plt.ylabel("Profit")

plt.xticks(rotation=75)

plt.tight_layout()

plt.savefig("top_profitable_products.png")

plt.show()

# =====================================================
# MONTHLY CATEGORY SALES ANALYSIS
# =====================================================

# Convert Order Date if needed
df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    errors='coerce'
)

# Create Month column
df['Month'] = df['Order Date'].dt.month_name()

# Group by Month and Category
monthly_category_sales = df.groupby(
    ['Month', 'Category']
)['Sales'].sum()

print("\nMONTHLY CATEGORY SALES")
print(monthly_category_sales)
# =====================================================
# INVENTORY & BUSINESS RECOMMENDATIONS
# =====================================================

print("\nBUSINESS RECOMMENDATIONS")

print("""
1. Maintain higher inventory levels for top-selling products.

2. Increase marketing efforts during low-sales periods.

3. Focus on high-profit products to improve profitability.

4. Use seasonal sales trends for better demand forecasting.

5. Offer discounts and bundle deals on low-performing products.

6. Optimize stock management for high-demand categories.
""")
# =====================================================
# KEY FINDINGS
# =====================================================

print("\nKEY FINDINGS")

print("""
1. Top-selling products were identified successfully.

2. Technology category generated the highest revenue.

3. Certain products showed high sales but lower profit margins.

4. Seasonal trends were observed in monthly category sales.

5. High-performing products should receive inventory priority.

6. Category analysis helps understand customer preferences.
""")