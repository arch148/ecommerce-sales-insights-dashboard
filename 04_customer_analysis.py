import pandas as pd

# Load datasets
customers = pd.read_csv("data_raw/olist_customers_dataset.csv")
orders = pd.read_csv("data_raw/olist_orders_dataset.csv")

# Merge customer + orders
merged = customers.merge(orders, on='customer_id')

# Count orders per unique customer
customer_orders = merged.groupby('customer_unique_id')['order_id'].count()

# Total customers
total_customers = customer_orders.shape[0]

# Repeat customers
repeat_customers = customer_orders[customer_orders > 1].count()

# One-time customers
one_time_customers = customer_orders[customer_orders == 1].count()

# Retention %
retention_rate = (repeat_customers / total_customers) * 100

print("="*50)
print("CUSTOMER RETENTION ANALYSIS")
print("="*50)

print(f"Total Unique Customers: {total_customers}")
print(f"Repeat Customers: {repeat_customers}")
print(f"One-time Customers: {one_time_customers}")
print(f"Retention Rate: {retention_rate:.2f}%")