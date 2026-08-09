import pandas as pd
import os

# -----------------------------
# LOAD CUSTOMERS DATA
# -----------------------------

input_file = "data/raw/customers.csv"

customers = pd.read_csv(input_file)

print("Original customer records:", len(customers))

# -----------------------------
# 1. REMOVE DUPLICATE CUSTOMERS
# -----------------------------

customers = customers.drop_duplicates(subset=["customer_id"])

print("After removing duplicates:", len(customers))

# -----------------------------
# 2. HANDLE MISSING EMAILS
# -----------------------------

customers["email"] = customers["email"].fillna("unknown@example.com")

# -----------------------------
# 3. STANDARDIZE TEXT COLUMNS
# -----------------------------

customers["name"] = customers["name"].str.strip()
customers["city"] = customers["city"].str.strip()

# -----------------------------
# 4. CONVERT SIGNUP DATE
# -----------------------------

customers["signup_date"] = pd.to_datetime(
    customers["signup_date"],
    errors="coerce"
)

# -----------------------------
# 5. REMOVE INVALID RECORDS
# -----------------------------

customers = customers.dropna(
    subset=["customer_id", "signup_date"]
)

# -----------------------------
# SAVE CLEANED DATA
# -----------------------------

output_folder = "data/cleaned"
os.makedirs(output_folder, exist_ok=True)

customers.to_csv(
    f"{output_folder}/customers_clean.csv",
    index=False
)

print("Customer data cleaned successfully!")
print("Cleaned records:", len(customers))

# -----------------------------
# LOAD PRODUCTS DATA
# -----------------------------

products = pd.read_csv("data/raw/products.csv")

print("\nOriginal product records:", len(products))

# -----------------------------
# 1. REMOVE DUPLICATE PRODUCTS
# -----------------------------

products = products.drop_duplicates(subset=["product_id"])

# -----------------------------
# 2. STANDARDIZE CATEGORY
# -----------------------------

products["category"] = products["category"].str.strip().str.title()

# -----------------------------
# 3. CONVERT PRICE TO NUMERIC
# -----------------------------

products["price"] = pd.to_numeric(
    products["price"],
    errors="coerce"
)

# -----------------------------
# 4. REMOVE INVALID PRICES
# -----------------------------

products = products[products["price"] > 0]

# -----------------------------
# 5. REMOVE MISSING IMPORTANT VALUES
# -----------------------------

products = products.dropna(
    subset=["product_id", "product_name", "category", "price"]
)

# -----------------------------
# SAVE CLEANED PRODUCTS
# -----------------------------

products.to_csv(
    "data/cleaned/products_clean.csv",
    index=False
)

print("Product data cleaned successfully!")
print("Cleaned product records:", len(products))

# -----------------------------
# LOAD ORDERS DATA
# -----------------------------

orders = pd.read_csv("data/raw/orders.csv")

print("\nOriginal order records:", len(orders))

# -----------------------------
# 1. REMOVE DUPLICATE ORDERS
# -----------------------------

orders = orders.drop_duplicates(subset=["order_id"])

# -----------------------------
# 2. CONVERT CUSTOMER ID
# -----------------------------

orders["customer_id"] = pd.to_numeric(
    orders["customer_id"],
    errors="coerce"
)

# -----------------------------
# 3. CONVERT ORDER DATE
# -----------------------------

orders["order_date"] = pd.to_datetime(
    orders["order_date"],
    errors="coerce"
)

# -----------------------------
# 4. STANDARDIZE ORDER STATUS
# -----------------------------

orders["status"] = orders["status"].str.strip().str.title()

# -----------------------------
# 5. REMOVE MISSING VALUES
# -----------------------------

orders = orders.dropna(
    subset=["order_id", "customer_id", "order_date", "status"]
)

# -----------------------------
# 6. VALIDATE CUSTOMER IDs
# -----------------------------

valid_customer_ids = set(customers["customer_id"])

orders = orders[
    orders["customer_id"].isin(valid_customer_ids)
]

# -----------------------------
# SAVE CLEANED ORDERS
# -----------------------------

orders.to_csv(
    "data/cleaned/orders_clean.csv",
    index=False
)

print("Order data cleaned successfully!")
print("Cleaned order records:", len(orders))

# -----------------------------
# LOAD ORDER ITEMS DATA
# -----------------------------

order_items = pd.read_csv("data/raw/order_items.csv")

print("\nOriginal order item records:", len(order_items))

# -----------------------------
# 1. REMOVE DUPLICATES
# -----------------------------

order_items = order_items.drop_duplicates(
    subset=["order_item_id"]
)

# -----------------------------
# 2. CONVERT NUMERIC COLUMNS
# -----------------------------

order_items["order_id"] = pd.to_numeric(
    order_items["order_id"],
    errors="coerce"
)

order_items["product_id"] = pd.to_numeric(
    order_items["product_id"],
    errors="coerce"
)

order_items["quantity"] = pd.to_numeric(
    order_items["quantity"],
    errors="coerce"
)

order_items["unit_price"] = pd.to_numeric(
    order_items["unit_price"],
    errors="coerce"
)

# -----------------------------
# 3. HANDLE MISSING VALUES
# -----------------------------

order_items = order_items.dropna(
    subset=[
        "order_item_id",
        "order_id",
        "product_id",
        "quantity",
        "unit_price"
    ]
)

# -----------------------------
# 4. REMOVE INVALID QUANTITIES
# -----------------------------

order_items = order_items[
    order_items["quantity"] > 0
]

# -----------------------------
# 5. REMOVE INVALID PRICES
# -----------------------------

order_items = order_items[
    order_items["unit_price"] > 0
]

# -----------------------------
# 6. VALIDATE ORDER IDs
# -----------------------------

valid_order_ids = set(orders["order_id"])

order_items = order_items[
    order_items["order_id"].isin(valid_order_ids)
]

# -----------------------------
# 7. VALIDATE PRODUCT IDs
# -----------------------------

valid_product_ids = set(products["product_id"])

order_items = order_items[
    order_items["product_id"].isin(valid_product_ids)
]

# -----------------------------
# SAVE CLEANED DATA
# -----------------------------

order_items.to_csv(
    "data/cleaned/order_items_clean.csv",
    index=False
)

print("Order items data cleaned successfully!")
print("Cleaned order item records:", len(order_items))