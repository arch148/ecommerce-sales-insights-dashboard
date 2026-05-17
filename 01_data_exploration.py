import pandas as pd
import numpy as np

# Load datasets
customers = pd.read_csv("data_raw/olist_customers_dataset.csv")
orders = pd.read_csv("data_raw/olist_orders_dataset.csv")
order_items = pd.read_csv("data_raw/olist_order_items_dataset.csv")
payments = pd.read_csv("data_raw/olist_order_payments_dataset.csv")
reviews = pd.read_csv("data_raw/olist_order_reviews_dataset.csv")
products = pd.read_csv("data_raw/olist_products_dataset.csv")
sellers = pd.read_csv("data_raw/olist_sellers_dataset.csv")

datasets = {
    "Customers": customers,
    "Orders": orders,
    "Order Items": order_items,
    "Payments": payments,
    "Reviews": reviews,
    "Products": products,
    "Sellers": sellers
}

for name, df in datasets.items():
    print(f"\n{'='*50}")
    print(f"{name} Dataset")
    print(f"{'='*50}")
    print("Shape:", df.shape)
    print("\nColumns:")
    print(df.columns.tolist())
    print("\nMissing Values:")
    print(df.isnull().sum())