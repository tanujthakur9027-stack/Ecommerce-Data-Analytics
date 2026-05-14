import pandas as pd
import matplotlib.pyplot as plt
# =========================================================
# Load Dataset
# =========================================================
df = pd.read_csv(
    r"C:\Users\Tanuj kumar singh\Downloads\Ecommerce_Project\cleaned_data\data.csv",
    encoding='latin1'
)

print(df.head())
# =========================================================
#CHECK COLUMNS
# =========================================================
print("\nDATASET COLUMNS")
print(df.columns.tolist())
# =====================================================
# CATEGORY SALES ANALYSIS
# =====================================================

category_sales = df.groupby('Category').agg({

    'Sales': 'sum',

    'Profit': 'sum',

    'Quantity': 'sum'

})

# Sort by Sales
category_sales = category_sales.sort_values(
    by='Sales',
    ascending=False
)

print("\nCATEGORY SALES ANALYSIS")

print(category_sales)
# =====================================================
# CATEGORY SALES BAR CHART
# =====================================================

plt.figure(figsize=(10,6))

category_sales['Sales'].plot(
    kind='bar'
)

plt.title("Sales by Product Category")

plt.xlabel("Category")

plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("category_sales_analysis.png")

plt.show()
# =====================================================
# CATEGORY BUSINESS INSIGHTS
# =====================================================

print("\nBUSINESS OPPORTUNITIES - PRODUCT CATEGORIES")

print("""
1. High-performing product categories should receive increased inventory investment.

2. Categories with strong profit margins can be prioritized in marketing campaigns.

3. Low-performing categories may require discount strategies or product improvements.

4. Businesses can expand product variety in top-selling categories.

5. Seasonal demand patterns should guide inventory planning.
""")
# =====================================================
# REGIONAL SALES ANALYSIS
# =====================================================

regional_sales = df.groupby('Region').agg({

    'Sales': 'sum',

    'Profit': 'sum',

    'Quantity': 'sum'

})

# Sort by Sales
regional_sales = regional_sales.sort_values(
    by='Sales',
    ascending=False
)

print("\nREGIONAL SALES ANALYSIS")

print(regional_sales)
# =====================================================
# REGIONAL SALES CHART
# =====================================================

plt.figure(figsize=(10,6))

regional_sales['Sales'].plot(
    kind='bar'
)

plt.title("Regional Sales Performance")

plt.xlabel("Region")

plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("regional_sales_analysis.png")

plt.show()
# =====================================================
# REGIONAL BUSINESS INSIGHTS
# =====================================================

print("\nREGIONAL BUSINESS OPPORTUNITIES")

print("""
1. High-sales regions should receive stronger marketing investments.

2. Businesses can optimize warehouse and logistics operations in high-demand regions.

3. Low-performing regions may require targeted promotions and pricing strategies.

4. Regional customer preferences should guide localized product recommendations.

5. Expansion strategies can focus on regions with growing sales trends.
""")
# =====================================================
# HIGH-VALUE CUSTOMER ANALYSIS
# =====================================================

high_value_customers = df.groupby('Customer ID').agg({

    'Sales': 'sum',

    'Profit': 'sum',

    'Quantity': 'sum'

})

# Sort by Sales
high_value_customers = high_value_customers.sort_values(
    by='Sales',
    ascending=False
)

print("\nTOP HIGH-VALUE CUSTOMERS")

print(high_value_customers.head(10))
# =====================================================
# CATEGORY PURCHASE ANALYSIS
# =====================================================

category_quantity = df.groupby('Category')['Quantity'].sum()

print("\nCATEGORY PURCHASE ANALYSIS")

print(category_quantity)
# =====================================================
# UPSELLING & CROSS-SELLING INSIGHTS
# =====================================================

print("\nUPSELLING & CROSS-SELLING OPPORTUNITIES")

print("""
1. High-value customers can be targeted with premium product recommendations.

2. Frequently purchased categories can be bundled together for combo offers.

3. Personalized recommendations can increase average order value.

4. Cross-selling accessories and complementary products can boost revenue.

5. Loyalty rewards and exclusive offers can improve customer retention.
""")