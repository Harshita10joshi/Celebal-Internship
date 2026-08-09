import pandas as pd

# -----------------------------
# LOAD CLEANED DATA
# -----------------------------

customers = pd.read_csv("data/cleaned/customers_clean.csv")
products = pd.read_csv("data/cleaned/products_clean.csv")
orders = pd.read_csv("data/cleaned/orders_clean.csv")
order_items = pd.read_csv("data/cleaned/order_items_clean.csv")

print("====================================")
print("     DATA VALIDATION REPORT")
print("====================================")

# -----------------------------
# 1. CHECK DUPLICATES
# -----------------------------

print("\n1. DUPLICATE CHECK")

print("Duplicate customers:",
      customers["customer_id"].duplicated().sum())

print("Duplicate products:",
      products["product_id"].duplicated().sum())

print("Duplicate orders:",
      orders["order_id"].duplicated().sum())

print("Duplicate order items:",
      order_items["order_item_id"].duplicated().sum())


# -----------------------------
# 2. CHECK MISSING VALUES
# -----------------------------

print("\n2. MISSING VALUE CHECK")

print("Customers missing values:",
      customers.isnull().sum().sum())

print("Products missing values:",
      products.isnull().sum().sum())

print("Orders missing values:",
      orders.isnull().sum().sum())

print("Order items missing values:",
      order_items.isnull().sum().sum())


# -----------------------------
# 3. CHECK INVALID PRICES
# -----------------------------

print("\n3. PRICE VALIDATION")

invalid_prices = (products["price"] <= 0).sum()

print("Invalid product prices:", invalid_prices)


# -----------------------------
# 4. CHECK INVALID QUANTITIES
# -----------------------------

print("\n4. QUANTITY VALIDATION")

invalid_quantities = (order_items["quantity"] <= 0).sum()

print("Invalid quantities:", invalid_quantities)


# -----------------------------
# 5. CHECK ORDER → CUSTOMER
# -----------------------------

print("\n5. ORDER-CUSTOMER INTEGRITY")

invalid_customer_orders = ~orders["customer_id"].isin(
    customers["customer_id"]
)

print(
    "Orders with invalid customer:",
    invalid_customer_orders.sum()
)


# -----------------------------
# 6. CHECK ORDER ITEM → ORDER
# -----------------------------

print("\n6. ORDER ITEM → ORDER INTEGRITY")

invalid_order_items = ~order_items["order_id"].isin(
    orders["order_id"]
)

print(
    "Order items with invalid order:",
    invalid_order_items.sum()
)


# -----------------------------
# 7. CHECK ORDER ITEM → PRODUCT
# -----------------------------

print("\n7. ORDER ITEM → PRODUCT INTEGRITY")

invalid_product_items = ~order_items["product_id"].isin(
    products["product_id"]
)

print(
    "Order items with invalid product:",
    invalid_product_items.sum()
)


# -----------------------------
# FINAL RESULT
# -----------------------------

if (
    customers["customer_id"].duplicated().sum() == 0
    and products["product_id"].duplicated().sum() == 0
    and orders["order_id"].duplicated().sum() == 0
    and order_items["order_item_id"].duplicated().sum() == 0
    and customers.isnull().sum().sum() == 0
    and products.isnull().sum().sum() == 0
    and orders.isnull().sum().sum() == 0
    and order_items.isnull().sum().sum() == 0
    and invalid_prices == 0
    and invalid_quantities == 0
    and invalid_customer_orders.sum() == 0
    and invalid_order_items.sum() == 0
    and invalid_product_items.sum() == 0
):
    print("\n====================================")
    print("VALIDATION PASSED")
    print("All cleaned data is valid.")
    print("====================================")
else:
    print("\n====================================")
    print("VALIDATION FAILED")
    print("Some data quality issues remain.")
    print("====================================")