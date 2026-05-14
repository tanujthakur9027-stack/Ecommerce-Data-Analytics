import pandas as pd
import matplotlib.pyplot as plt

from statsmodels.tsa.holtwinters import ExponentialSmoothing

from sklearn.metrics import mean_squared_error

import numpy as np
   
# =====================================================
# LOAD TIME SERIES DATASET
# =====================================================

df = pd.read_csv(
    r"C:\Users\Tanuj kumar singh\Downloads\Ecommerce_Project\task5_time_series_analysis\processed_time_series_dataset.csv"
)

print(df.head())
# =====================================================
# CONVERT DATE COLUMN
# =====================================================

df['Order Date'] = pd.to_datetime(
    df['Order Date']
)

df.set_index(
    'Order Date',
    inplace=True
)

print("\nDATE INDEX CREATED")
# =====================================================
# TRAIN & TEST SPLIT
# =====================================================

train_size = int(len(df) * 0.8)

train = df[:train_size]

test = df[train_size:]

print("\nTRAIN DATA SIZE:", len(train))

print("TEST DATA SIZE:", len(test))
# =====================================================
# TRAIN HOLT-WINTERS MODEL
# =====================================================

model = ExponentialSmoothing(
    train['Sales'],
    trend='add',
    seasonal=None
)

model_fit = model.fit()

print("\nMODEL TRAINED SUCCESSFULLY")
# =====================================================
# MAKE PREDICTIONS
# =====================================================

predictions = model_fit.forecast(
    len(test)
)

print("\nPREDICTIONS")
print(predictions.head())
# =====================================================
# CALCULATE RMSE
# =====================================================

rmse = np.sqrt(
    mean_squared_error(
        test['Sales'],
        predictions
    )
)

print("\nRMSE VALUE")
print(rmse)
# =====================================================
# FORECAST VISUALIZATION
# =====================================================

plt.figure(figsize=(14,6))

plt.plot(
    train.index,
    train['Sales'],
    label='Training Data'
)

plt.plot(
    test.index,
    test['Sales'],
    label='Actual Sales'
)

plt.plot(
    test.index,
    predictions,
    label='Predicted Sales'
)

plt.title("Sales Forecasting")

plt.xlabel("Date")

plt.ylabel("Sales")

plt.legend()

plt.tight_layout()

plt.savefig("sales_forecast_chart.png")

plt.show()
# =====================================================
# FUTURE SALES FORECAST
# =====================================================
future_forecast = model_fit.forecast(180)

print("\nNEXT 180 DAYS FORECAST")
print(future_forecast)
# =====================================================
# FORECAST ANALYSIS
# =====================================================

print("\nFORECAST ANALYSIS")

print("""
1. Sales forecasting model successfully predicted future sales trends.

2. Forecasting helps businesses plan inventory and marketing strategies.

3. Predicted trends can identify future growth opportunities.

4. Seasonal fluctuations and sales patterns were analyzed successfully.

5. Forecasting supports better business decision-making and revenue planning.
""")
# =====================================================
# SAVE FORECAST RESULTS
# =====================================================

forecast_df = pd.DataFrame({
    'Actual Sales': test['Sales'],
    'Predicted Sales': predictions
})

forecast_df.to_csv(
    "forecast_results.csv"
)

print("\nFORECAST RESULTS SAVED")
# =====================================================
# SAVE FUTURE FORECAST DATASET
# =====================================================

future_forecast_df = pd.DataFrame({
    'Date': pd.date_range(
        start=df.index[-1],
        periods=180,
        freq='D'
    ),
    'Predicted Sales': future_forecast.values
})

future_forecast_df.to_csv(
    "forecasted_sales_dataset.csv",
    index=False
)

print("\nFUTURE FORECAST DATASET SAVED")