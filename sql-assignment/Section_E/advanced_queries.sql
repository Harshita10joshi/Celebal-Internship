USE ecommerce_sales;
-- ==========================================
-- Section E - Advanced Concepts
-- ==========================================

-- Q24. Classify products into price tiers using CASE

SELECT
    product_name,
    unit_price,
    CASE
        WHEN unit_price < 1000 THEN 'Budget'
        WHEN unit_price BETWEEN 1000 AND 3000 THEN 'Mid-Range'
        ELSE 'Premium'
    END AS price_tier
FROM products;

-- Q25. Count Delivered vs Not Delivered orders in one row

SELECT
    SUM(CASE
            WHEN status = 'Delivered' THEN 1
            ELSE 0
        END) AS Delivered_Orders,

    SUM(CASE
            WHEN status <> 'Delivered' THEN 1
            ELSE 0
        END) AS Not_Delivered_Orders
FROM `orders`;

-- ==========================================================
-- Q26.
-- ACID Properties
--
-- A - Atomicity
-- Either all operations of a transaction succeed,
-- or none of them are saved.
--
-- C - Consistency
-- Database always remains in a valid state before
-- and after a transaction.
--
-- I - Isolation
-- Multiple transactions do not interfere with each other.
--
-- D - Durability
-- Once committed, data remains saved even if the
-- system crashes.
--
-- Example:
-- Bank Transfer
--
-- Account A → Debit ₹500
-- Account B → Credit ₹500
--
-- If credit fails, debit is also rolled back.
-- This ensures Atomicity.
--
-- Balance rules remain valid (Consistency).
-- Other users cannot see incomplete transfer (Isolation).
-- Once committed, transfer remains stored (Durability).
-- ==========================================================

-- Q27. Transaction Example

START TRANSACTION;

-- Step 1: Insert new order

INSERT INTO `orders`
(order_id, customer_id, order_date, status, total_amount)
VALUES
(1011, 102, CURDATE(), 'Pending', 1598.00);

-- Step 2: Insert order items

INSERT INTO order_items
(item_id, order_id, product_id, quantity, unit_price, discount_pct)
VALUES
(5016, 1011, 206, 1, 1299.00, 0);

INSERT INTO order_items
(item_id, order_id, product_id, quantity, unit_price, discount_pct)
VALUES
(5017, 1011, 208, 1, 599.00, 0);

-- Step 3: Update stock quantity

UPDATE products
SET stock_qty = stock_qty - 1
WHERE product_id = 206;

UPDATE products
SET stock_qty = stock_qty - 1
WHERE product_id = 208;

-- Step 4:
-- If everything is successful

COMMIT;

-- If any query fails before COMMIT,
-- execute:

-- ROLLBACK;