import pandas as pd

reviews = pd.read_csv("data_raw/olist_order_reviews_dataset.csv")

avg_review = reviews['review_score'].mean()

bad_reviews = reviews[reviews['review_score'] <= 2].shape[0]
good_reviews = reviews[reviews['review_score'] >= 4].shape[0]
total_reviews = reviews.shape[0]

bad_review_percentage = (bad_reviews / total_reviews) * 100
good_review_percentage = (good_reviews / total_reviews) * 100

print("="*50)
print("CUSTOMER SATISFACTION ANALYSIS")
print("="*50)

print(f"Average Review Score: {avg_review:.2f}")
print(f"Bad Reviews (1–2 stars): {bad_reviews}")
print(f"Good Reviews (4–5 stars): {good_reviews}")
print(f"Bad Review Percentage: {bad_review_percentage:.2f}%")
print(f"Good Review Percentage: {good_review_percentage:.2f}%")