import pandas as pd

# Load datasets
orders = pd.read_csv("data_raw/olist_orders_dataset.csv")
payments = pd.read_csv("data_raw/olist_order_payments_dataset.csv")

# Convert date
orders['order_purchase_timestamp'] = pd.to_datetime(
    orders['order_purchase_timestamp']
)

# Total Revenue
total_revenue = payments['payment_value'].sum()

# Total Orders
total_orders = orders['order_id'].nunique()

# Average Order Value
avg_order_value = total_revenue / total_orders

# Monthly revenue
merged = orders.merge(payments, on='order_id')

merged['month'] = merged['order_purchase_timestamp'].dt.to_period('M')

monthly_revenue = merged.groupby('month')['payment_value'].sum()

print("="*50)
print("REVENUE KPI ANALYSIS")
print("="*50)

print(f"Total Revenue: {total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Average Order Value: {avg_order_value:,.2f}")

print("\nMonthly Revenue:")
print(monthly_revenue.head(12))