import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta
import os

fake = Faker()
random.seed(42)

# Create output folder
output_folder = "data/raw"
os.makedirs(output_folder, exist_ok=True)

# -----------------------------
# 1. CUSTOMERS DATA
# -----------------------------

customers = []

for i in range(1, 501):
    customers.append({
        "customer_id": i,
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "signup_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        )
    })

customers_df = pd.DataFrame(customers)

# Intentional inconsistencies
customers_df.loc[10, "email"] = None
customers_df.loc[25, "email"] = None

# Duplicate customer
customers_df = pd.concat(
    [customers_df, customers_df.iloc[[50]]],
    ignore_index=True
)

# -----------------------------
# 2. PRODUCTS DATA
# -----------------------------

categories = [
    "Electronics",
    "Fashion",
    "Home",
    "Beauty",
    "Sports"
]

products = []

for i in range(1, 101):
    products.append({
        "product_id": i,
        "product_name": fake.catch_phrase(),
        "category": random.choice(categories),
        "price": round(random.uniform(100, 50000), 2)
    })

products_df = pd.DataFrame(products)

# Intentional inconsistencies
products_df.loc[5, "price"] = -500
products_df.loc[15, "category"] = "electronics"
products_df.loc[25, "category"] = " ELECTRONICS "

# -----------------------------
# 3. ORDERS DATA
# -----------------------------

orders = []

start_date = datetime.now() - timedelta(days=730)

for i in range(1, 2001):

    order_date = start_date + timedelta(
        days=random.randint(0, 729)
    )

    orders.append({
        "order_id": i,
        "customer_id": random.randint(1, 500),
        "order_date": order_date.strftime("%Y-%m-%d"),
        "status": random.choice([
            "Completed",
            "Completed",
            "Completed",
            "Cancelled",
            "Returned"
        ])
    })

orders_df = pd.DataFrame(orders)

# Intentional invalid customer ID
orders_df.loc[20, "customer_id"] = 9999

# Duplicate order
orders_df = pd.concat(
    [orders_df, orders_df.iloc[[100]]],
    ignore_index=True
)

# -----------------------------
# 4. ORDER ITEMS DATA
# -----------------------------

order_items = []

item_id = 1

for order_id in orders_df["order_id"].unique():

    number_of_items = random.randint(1, 4)

    for _ in range(number_of_items):

        product_id = random.randint(1, 100)
        quantity = random.randint(1, 5)

        product_price = products_df.loc[
            products_df["product_id"] == product_id,
            "price"
        ].iloc[0]

        order_items.append({
            "order_item_id": item_id,
            "order_id": order_id,
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": product_price
        })

        item_id += 1

order_items_df = pd.DataFrame(order_items)

# Intentional inconsistencies
order_items_df.loc[10, "quantity"] = None
order_items_df.loc[20, "quantity"] = -2

# -----------------------------
# SAVE CSV FILES
# -----------------------------

customers_df.to_csv(
    f"{output_folder}/customers.csv",
    index=False
)

products_df.to_csv(
    f"{output_folder}/products.csv",
    index=False
)

orders_df.to_csv(
    f"{output_folder}/orders.csv",
    index=False
)

order_items_df.to_csv(
    f"{output_folder}/order_items.csv",
    index=False
)

print("Dataset generation completed successfully!")
print()
print("Files created:")
print("1. customers.csv")
print("2. products.csv")
print("3. orders.csv")
print("4. order_items.csv")