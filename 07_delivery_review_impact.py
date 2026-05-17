import pandas as pd

orders = pd.read_csv("data_raw/olist_orders_dataset.csv")
reviews = pd.read_csv("data_raw/olist_order_reviews_dataset.csv")

# Convert dates
orders['order_delivered_customer_date'] = pd.to_datetime(
    orders['order_delivered_customer_date']
)

orders['order_estimated_delivery_date'] = pd.to_datetime(
    orders['order_estimated_delivery_date']
)

# Delay
orders['delay_days'] = (
    orders['order_delivered_customer_date'] -
    orders['order_estimated_delivery_date']
).dt.days

# Merge
merged = orders.merge(reviews, on='order_id')

# Late vs on-time
late_orders = merged[merged['delay_days'] > 0]
on_time_orders = merged[merged['delay_days'] <= 0]

late_avg_review = late_orders['review_score'].mean()
on_time_avg_review = on_time_orders['review_score'].mean()

print("="*50)
print("DELIVERY IMPACT ON CUSTOMER SATISFACTION")
print("="*50)

print(f"Late Orders Avg Review: {late_avg_review:.2f}")
print(f"On-Time Orders Avg Review: {on_time_avg_review:.2f}")