import pandas as pd

orders = pd.read_csv("data_raw/olist_orders_dataset.csv")

# Convert dates
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

# Actual delivery days
orders['actual_delivery_days'] = (
    orders['order_delivered_customer_date'] - orders['order_purchase_timestamp']
).dt.days

# Delay days
orders['delay_days'] = (
    orders['order_delivered_customer_date'] - orders['order_estimated_delivery_date']
).dt.days

avg_delivery = orders['actual_delivery_days'].mean()
late_orders = orders[orders['delay_days'] > 0].shape[0]
total_orders = orders.shape[0]
late_percentage = (late_orders / total_orders) * 100

print("="*50)
print("DELIVERY PERFORMANCE ANALYSIS")
print("="*50)

print(f"Average Delivery Time: {avg_delivery:.2f} days")
print(f"Late Deliveries: {late_orders}")
print(f"Late Delivery Percentage: {late_percentage:.2f}%")