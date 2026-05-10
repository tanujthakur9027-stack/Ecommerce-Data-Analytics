# =====================================================
# TASK 3 - MONTHLY & YEARLY SALES TREND ANALYSIS
# =====================================================

# =====================================================
# IMPORT LIBRARIES
# =====================================================

import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# LOAD CLEANED DATASET
# =====================================================

df = pd.read_csv(
    r"C:\Users\Tanuj kumar singh\Downloads\Ecommerce_Project\cleaned_data\data.csv",
    encoding='latin1'
)

print("Dataset Loaded Successfully!\n")

# =====================================================
# DISPLAY FIRST 5 ROWS
# =====================================================

print("FIRST 5 ROWS")
print(df.head())

# =====================================================
# CONVERT ORDER DATE COLUMN
# =====================================================

df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    errors='coerce'
)

print("\nDate Conversion Completed!")

# =====================================================
# CREATE YEAR & MONTH COLUMNS
# =====================================================

df['Year'] = df['Order Date'].dt.year

df['Month'] = df['Order Date'].dt.month_name()

print("\nYear and Month Columns Created!")

# =====================================================
# MONTHLY SALES ANALYSIS
# =====================================================

monthly_sales = df.groupby('Month')['Sales'].sum()

print("\nMONTHLY SALES")
print(monthly_sales)

# =====================================================
# YEARLY SALES ANALYSIS
# =====================================================

yearly_sales = df.groupby('Year')['Sales'].sum()

print("\nYEARLY SALES")
print(yearly_sales)

# =====================================================
# IDENTIFY BEST & WORST MONTHS
# =====================================================

best_month = monthly_sales.idxmax()

worst_month = monthly_sales.idxmin()

print("\nBEST SALES MONTH:", best_month)

print("WORST SALES MONTH:", worst_month)

# =====================================================
# IDENTIFY BEST & WORST YEARS
# =====================================================

best_year = yearly_sales.idxmax()

worst_year = yearly_sales.idxmin()

print("\nBEST SALES YEAR:", best_year)

print("WORST SALES YEAR:", worst_year)

# =====================================================
# MONTHLY SALES LINE CHART
# =====================================================

plt.figure(figsize=(12,6))

monthly_sales.plot(
    kind='line',
    marker='o'
)

plt.title("Monthly Sales Trend")

plt.xlabel("Month")

plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.grid(True)

plt.tight_layout()
plt.savefig("monthly_sales_trend.png")
plt.show()

# =====================================================
# YEARLY SALES BAR CHART
# =====================================================

plt.figure(figsize=(8,5))

yearly_sales.plot(
    kind='bar'
)

plt.title("Yearly Sales Trend")

plt.xlabel("Year")

plt.ylabel("Total Sales")

plt.tight_layout()
plt.savefig("yearly_sales_trend.png")8
plt.show()

# =====================================================
# TOP 5 SALES MONTHS
# =====================================================

top_months = monthly_sales.sort_values(
    ascending=False
).head(5)

print("\nTOP 5 SALES MONTHS")
print(top_months)

# =====================================================
# LOWEST 5 SALES MONTHS
# =====================================================

lowest_months = monthly_sales.sort_values(
    ascending=True
).head(5)

print("\nLOWEST 5 SALES MONTHS")
print(lowest_months)

# =====================================================
# SAVE MONTHLY & YEARLY SALES SUMMARY
# =====================================================

monthly_sales.to_csv(
    "monthly_sales_summary.csv"
)

yearly_sales.to_csv(
    "yearly_sales_summary.csv"
)

print("\nSales Summary CSV Files Saved!")

# =====================================================
# FINAL INSIGHTS
# =====================================================

print("\nKEY INSIGHTS")

print("""
1. Monthly sales trends were analyzed successfully.

2. Yearly revenue growth patterns identified.

3. Best and worst performing sales months detected.

4. Peak sales periods can help businesses plan inventory.

5. Seasonal trends can support marketing strategies.

6. Dataset is ready for advanced business analysis.
""")

# =====================================================
# TASK 3 COMPLETED
# =====================================================*8