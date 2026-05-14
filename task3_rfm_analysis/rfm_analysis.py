import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv(
    r"C:\Users\Tanuj kumar singh\Downloads\Ecommerce_Project\cleaned_data\data.csv",
    encoding='latin1'
)

print(df.head())
# =====================================================
# CONVERT ORDER DATE
# =====================================================

df['Order Date'] = pd.to_datetime(
    df['Order Date'],
    errors='coerce'
)

print("\nDate Conversion Successful")
# =====================================================
# CREATE REFERENCE DATE
# =====================================================
reference_date = df['Order Date'].max() + pd.Timedelta(days=1)
print("\nReference Date Created:", reference_date)
# =====================================================
# CALCULATE RFM METRICS
rfm = df.groupby('Customer ID').agg({
    'Order Date': lambda x: (reference_date - x.max()).days,
    'Order ID': 'count',
    'Sales': 'sum'
})
# Rename columns
rfm.columns = ['Recency', 'Frequency', 'Monetary']
print("\nRFM TABLE")
print(rfm.head())
# =====================================================
# RFM SCORING
rfm['R_Score'] = pd.qcut(rfm['Recency'], 5, labels=[5, 4, 3, 2, 1])
rfm['F_Score'] = pd.qcut(rfm['Frequency'], 5, labels=[1, 2, 3, 4, 5])
rfm['M_Score'] = pd.qcut(rfm['Monetary'], 5, labels=[1, 2, 3, 4, 5])
# Combine RFM scores into a single string
rfm['RFM_Score'] = rfm['R_Score'].astype(str) + rfm['F_Score'].astype(str) + rfm['M_Score'].astype(str)
print("\nRFM SCORES")
print(rfm['RFM_Score'].head())
# =====================================================
# RFM SEGMENTATION
def segment_customer(row):
    if row['RFM_Score'] == '555':
        return 'Best Customers'
    elif row['RFM_Score'] in ['455', '545', '554']:
        return 'Loyal Customers'
    elif row['RFM_Score'] in ['355', '455', '545']:
        return 'Potential Loyalists'
    elif row['RFM_Score'] in ['255', '355', '455']:
        return 'New Customers'
    elif row['RFM_Score'] in ['155', '255', '355']:
        return 'Promising Customers'
    elif row['RFM_Score'] in ['111', '211', '311']:
        return 'At Risk Customers'
    else:
        return 'Others'
rfm['Segment'] = rfm.apply(segment_customer, axis=1)
print("\nRFM SEGMENTS")
print(rfm['Segment'].head())
# =====================================================
# SEGMENT COUNTS
segment_counts = rfm['Segment'].value_counts()
print("\nSEGMENT COUNTS")
print(segment_counts)
# =====================================================
# Customer SEGMENT BAR CHART
plt.figure(figsize=(10, 6))
segment_counts.plot(kind='bar', color='skyblue')
plt.title('Customer Segments')
plt.xlabel('Segment')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("customer_segmenyts_bar_chart.png")
plt.show()
# =====================================================
# BUSINESS RECOMMENDATIONS
# =====================================================

print("\nBUSINESS RECOMMENDATIONS")

print("""
1. Reward Champions with exclusive offers and loyalty programs.

2. Encourage Loyal Customers with personalized recommendations.

3. Convert Potential Loyalists into regular buyers using targeted promotions.

4. Re-engage At Risk customers through discounts and reminder campaigns.

5. Win back Lost Customers using special offers and email marketing.

6. Focus marketing investments on high-value customer segments.
""")
# =====================================================
# SAVE FINAL RFM DATASET
# =====================================================

rfm.to_csv(
    "rfm_customer_analysis.csv"
)

print("\nRFM Dataset Saved Successfully!")

# =====================================================
# CUSTOMER SEGMENT PIE CHART
# =====================================================

plt.figure(figsize=(8,8))

segment_counts.plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Customer Segment Distribution")

plt.ylabel("")

plt.tight_layout()

plt.savefig("customer_segment_pie_chart.png")

plt.show()
# =====================================================
# RFM SCATTER PLOT
plt.figure(figsize=(10,6))
plt.scatter(
    rfm['Recency'],
    rfm['Monetary']/10,
    c=rfm['Frequency'],
    cmap='viridis',
    alpha=0.6
)

plt.title("Rercency vs Frequency vs Monetary ")
plt.xlabel("Recency (Days Since Last Purchase)")
plt.ylabel("Monetary Value (Scaled)")
plt.colorbar(label='Frequency')
plt.tight_layout()
plt.savefig("rfm_scatter_plot.png")
plt.show()
# =====================================================
# RFM HEATMAP
# =====================================================

import seaborn as sns

plt.figure(figsize=(8,6))

heatmap_data = rfm.pivot_table(
    values='Monetary',
    index='R_Score',
    columns='F_Score',
    aggfunc='mean'
)

sns.heatmap(
    heatmap_data,
    annot=True,
    fmt=".0f",
    cmap="YlGnBu"
)

plt.title("RFM Heatmap")

plt.tight_layout()

plt.savefig("rfm_heatmap.png")

plt.show()

    


