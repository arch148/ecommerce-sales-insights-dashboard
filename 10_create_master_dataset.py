import pandas as pd

customers = pd.read_csv("data_raw/olist_customers_dataset.csv")
orders = pd.read_csv("data_raw/olist_orders_dataset.csv")
order_items = pd.read_csv("data_raw/olist_order_items_dataset.csv")
payments = pd.read_csv("data_raw/olist_order_payments_dataset.csv")
reviews = pd.read_csv("data_raw/olist_order_reviews_dataset.csv")
products = pd.read_csv("data_raw/olist_products_dataset.csv")
sellers = pd.read_csv("data_raw/olist_sellers_dataset.csv")

# Date conversion
orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['order_delivered_customer_date'] = pd.to_datetime(orders['order_delivered_customer_date'])
orders['order_estimated_delivery_date'] = pd.to_datetime(orders['order_estimated_delivery_date'])

# Merge everything
master = orders.merge(customers, on='customer_id', how='left')
master = master.merge(order_items, on='order_id', how='left')
master = master.merge(payments, on='order_id', how='left')
master = master.merge(reviews, on='order_id', how='left')
master = master.merge(products, on='product_id', how='left')
master = master.merge(sellers, on='seller_id', how='left')

# Feature engineering
master['delivery_days'] = (
    master['order_delivered_customer_date'] -
    master['order_purchase_timestamp']
).dt.days

master['delay_days'] = (
    master['order_delivered_customer_date'] -
    master['order_estimated_delivery_date']
).dt.days

master['is_late'] = master['delay_days'].apply(
    lambda x: 1 if pd.notnull(x) and x > 0 else 0
)

# Save
master.to_csv("data_cleaned/master_ecommerce_dataset.csv", index=False)

print("MASTER DATASET CREATED SUCCESSFULLY")
print(master.shape)