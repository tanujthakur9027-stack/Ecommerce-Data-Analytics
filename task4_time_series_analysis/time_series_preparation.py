import pandas as pd
import matplotlib.pyplot as plt
# Load the cleaned dataset
df = pd.read_csv(
    r"C:\Users\Tanuj kumar singh\Downloads\Ecommerce_Project\cleaned_data\data.csv",
    encoding='latin1'
)

print(df.head())
# =====================================================
# CONVERT ORDER DATE TO DATETIME
# =====================================================

df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    errors='coerce'
)

print("\nDATE CONVERSION SUCCESSFUL")
# =====================================================
# EXTRACT DATE COMPONENTS
# =====================================================

df['Year'] = df['Order Date'].dt.year

df['Month'] = df['Order Date'].dt.month

df['Day'] = df['Order Date'].dt.day

df['Week'] = df['Order Date'].dt.isocalendar().week

print("\nDATE COMPONENTS CREATED")
# =====================================================
# DAILY SALES AGGREGATION
# =====================================================

daily_sales = df.groupby(
    'Order Date'
)['Sales'].sum()

print("\nDAILY SALES")
print(daily_sales.head())
# =====================================================
# MONTHLY SALES AGGREGATION
# =====================================================

monthly_sales = df.groupby(
    ['Year', 'Month']
)['Sales'].sum()

print("\nMONTHLY SALES")
print(monthly_sales.head())
# =====================================================
# HANDLE MISSING DATES
# =====================================================

daily_sales = daily_sales.asfreq('D')

daily_sales = daily_sales.fillna(0)

print("\nMISSING DATES HANDLED")
# =====================================================
# SORT TIME SERIES DATA
# =====================================================

daily_sales = daily_sales.sort_index()

print("\nTIME SERIES SORTED SUCCESSFULLY")
# =====================================================
# DAILY SALES TREND CHART
# =====================================================

plt.figure(figsize=(14,6))

daily_sales.plot()

plt.title("Daily Sales Trend")

plt.xlabel("Date")

plt.ylabel("Sales")

plt.tight_layout()

plt.savefig("daily_sales_trend.png")

plt.show()
# =====================================================
# MONTHLY SALES TREND CHART
# =====================================================

monthly_sales_plot = df.groupby(
    ['Year', 'Month']
)['Sales'].sum().reset_index()

monthly_sales_plot['Year-Month'] = (
    monthly_sales_plot['Year'].astype(str)
    + '-'
    + monthly_sales_plot['Month'].astype(str)
)

plt.figure(figsize=(14,6))

plt.plot(
    monthly_sales_plot['Year-Month'],
    monthly_sales_plot['Sales']
)

plt.title("Monthly Sales Trend")

plt.xlabel("Year-Month")

plt.ylabel("Sales")

plt.xticks(rotation=90)

plt.tight_layout()

plt.savefig("monthly_sales_time_series.png")

plt.show()
# =====================================================
# HIGHEST & LOWEST SALES DAYS
# =====================================================

highest_sales_day = daily_sales.idxmax()

lowest_sales_day = daily_sales.idxmin()

print("\nHIGHEST SALES DAY")
print(highest_sales_day)

print("\nLOWEST SALES DAY")
print(lowest_sales_day)
# =====================================================
# SAVE PROCESSED TIME SERIES DATASET
# =====================================================

daily_sales.to_csv(
    "processed_time_series_dataset.csv"
)

print("\nTIME SERIES DATASET SAVED SUCCESSFULLY")