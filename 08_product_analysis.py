import pandas as pd

order_items = pd.read_csv("data_raw/olist_order_items_dataset.csv")
products = pd.read_csv("data_raw/olist_products_dataset.csv")

# Merge
merged = order_items.merge(products, on='product_id')

# Category revenue
category_revenue = (
    merged.groupby('product_category_name')['price']
    .sum()
    .sort_values(ascending=False)
)

print("="*50)
print("PRODUCT CATEGORY REVENUE ANALYSIS")
print("="*50)

print(category_revenue.head(15))