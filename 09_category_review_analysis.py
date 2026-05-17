import pandas as pd

order_items = pd.read_csv("data_raw/olist_order_items_dataset.csv")
products = pd.read_csv("data_raw/olist_products_dataset.csv")
reviews = pd.read_csv("data_raw/olist_order_reviews_dataset.csv")

# Merge
merged = order_items.merge(products, on='product_id')
merged = merged.merge(reviews, on='order_id')

# Category avg review
category_reviews = (
    merged.groupby('product_category_name')['review_score']
    .mean()
    .sort_values()
)

print("="*50)
print("CATEGORY CUSTOMER SATISFACTION ANALYSIS")
print("="*50)

print(category_reviews.head(15))