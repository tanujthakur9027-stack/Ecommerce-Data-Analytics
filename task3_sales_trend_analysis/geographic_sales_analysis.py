import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(
    r"C:\Users\Tanuj kumar singh\Downloads\Ecommerce_Project\cleaned_data\data.csv",
    encoding='latin1'                       
)       
print(df.head())
# =====================================================
# GEOGRAPHIC SALES ANALYSIS
# =====================================================
geographic_sales = df.groupby('State').agg({
    'Sales': 'sum',
    'Quantity': 'sum',
    'Profit': 'sum'
})
# Sort by highest sales
geographic_sales = geographic_sales.sort_values(
    by='Sales',
    ascending=False
)
# Top 10 States
top_10_states = geographic_sales.head(10)
print("\nTOP 10 STATES BY SALES")
print(top_10_states)
# =====================================================
# TOP 10 STATES BAR CHART
# =====================================================
plt.figure(figsize=(12,6))
top_10_states['Sales'].plot(
    kind='bar'
)
plt.title('Top 10 States by Sales')
plt.xlabel('State')
plt.ylabel('Total Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_10_states_sales.png")
plt.show()
# =====================================================
# LOWEST 5 STATES
# =====================================================

lowest_5_states = geographic_sales.tail(5)

print("\nLOWEST 5 STATES BY SALES")
print(lowest_5_states)
# =====================================================
# REGION-WISE SALES ANALYSIS
# =====================================================

region_sales = df.groupby('Region').agg({
    'Sales': 'sum',
    'Quantity': 'sum',
    'Profit': 'sum'
})

# Sort by Sales
region_sales = region_sales.sort_values(
    by='Sales',
    ascending=False
)

print("\nREGION-WISE SALES ANALYSIS")
print(region_sales)
# =====================================================
# REGION SALES PIE CHART
# =====================================================

plt.figure(figsize=(8,8))

region_sales['Sales'].plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Sales Distribution by Region")

plt.ylabel("")

plt.tight_layout()

plt.savefig("region_sales_distribution.png")

plt.show()
# =====================================================
# CITY-WISE SALES ANALYSIS
# =====================================================

city_sales = df.groupby('City').agg({
    'Sales': 'sum',
    'Profit': 'sum',
    'Quantity': 'sum'
})

# Sort by Sales
city_sales = city_sales.sort_values(
    by='Sales',
    ascending=False
)

# Top 10 Cities
top_cities = city_sales.head(10)

print("\nTOP 10 CITIES BY SALES")
print(top_cities)
# =====================================================
# TOP CITIES BAR CHART
# =====================================================

plt.figure(figsize=(12,6))

top_cities['Sales'].plot(
    kind='bar'
)

plt.title("Top 10 Cities by Sales")

plt.xlabel("City")

plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("top_cities_sales.png")

plt.show()
# =====================================================
# BUSINESS RECOMMENDATIONS
# =====================================================

print("\nBUSINESS RECOMMENDATIONS")

print("""
1. Focus marketing campaigns on high-performing states and cities.

2. Improve logistics and warehouse support in high-demand regions.

3. Launch promotional offers in low-performing regions.

4. Increase inventory availability for top-selling locations.

5. Analyze regional customer preferences for personalized marketing.

6. Expand business operations in regions with high sales potential.
""")
# =====================================================
# KEY FINDINGS
# =====================================================

print("\nKEY FINDINGS")

print("""
1. Geographic sales analysis identified high-performing states and cities.

2. Certain regions contributed significantly more revenue than others.

3. Urban cities generated higher sales compared to smaller cities.

4. Regional sales distribution helps optimize inventory planning.

5. Geographic trends can improve targeted marketing strategies.

6. Underperforming regions may require additional promotions and campaigns.
""")
