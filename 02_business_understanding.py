import pandas as pd

# Load datasets
customers = pd.read_csv("data_raw/olist_customers_dataset.csv")
orders = pd.read_csv("data_raw/olist_orders_dataset.csv")
order_items = pd.read_csv("data_raw/olist_order_items_dataset.csv")
payments = pd.read_csv("data_raw/olist_order_payments_dataset.csv")
reviews = pd.read_csv("data_raw/olist_order_reviews_dataset.csv")
products = pd.read_csv("data_raw/olist_products_dataset.csv")
sellers = pd.read_csv("data_raw/olist_sellers_dataset.csv")

print("Customers unique customer_id:", customers['customer_id'].nunique())
print("Orders unique order_id:", orders['order_id'].nunique())
print("Order Items unique order_id:", order_items['order_id'].nunique())
print("Payments unique order_id:", payments['order_id'].nunique())
print("Reviews unique order_id:", reviews['order_id'].nunique())