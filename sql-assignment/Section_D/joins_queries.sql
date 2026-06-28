USE ecommerce_sales;
-- ==========================================
-- Section D - Joins & Relationships
-- ==========================================

-- Q19. Display each order with customer details

SELECT
    o.order_id,
    o.order_date,
    c.first_name,
    c.last_name,
    o.total_amount
FROM `orders` o
INNER JOIN customers c
ON o.customer_id = c.customer_id;

-- Q20. List ALL customers and their orders

SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    o.order_id,
    o.order_date,
    o.status,
    o.total_amount
FROM customers c
LEFT JOIN `orders` o
ON c.customer_id = o.customer_id;

-- Q21. Display order items with product details

SELECT
    o.order_id,
    p.product_name,
    oi.quantity,
    oi.unit_price,
    oi.discount_pct
FROM `orders` o
INNER JOIN order_items oi
ON o.order_id = oi.order_id
INNER JOIN products p
ON oi.product_id = p.product_id;

-- ==========================================================
-- Q22.
-- Difference between LEFT JOIN and RIGHT JOIN
--
-- LEFT JOIN:
-- Returns all rows from the left table and matching
-- rows from the right table.
--
-- RIGHT JOIN:
-- Returns all rows from the right table and matching
-- rows from the left table.
--
-- FULL OUTER JOIN:
-- Returns all matching and non-matching rows from
-- both tables.
-- MySQL does not support FULL OUTER JOIN directly.
-- ==========================================================

-- Example of LEFT JOIN

SELECT
    c.first_name,
    o.order_id
FROM customers c
LEFT JOIN `orders` o
ON c.customer_id = o.customer_id;

-- Example of RIGHT JOIN

SELECT
    c.first_name,
    o.order_id
FROM customers c
RIGHT JOIN `orders` o
ON c.customer_id = o.customer_id;

-- ==========================================================
-- Q23.
-- Foreign Key Relationships
--
-- 1. orders.customer_id
--    → customers.customer_id
--
-- 2. order_items.order_id
--    → orders.order_id
--
-- 3. order_items.product_id
--    → products.product_id
--
-- If customer_id = 999 does not exist,
-- MySQL will throw a FOREIGN KEY constraint error.
-- ==========================================================

-- Example

INSERT INTO `orders`
VALUES
(1015,
999,
'2024-09-01',
'Pending',
1500.00);

-- Expected:
-- ERROR: Cannot add or update a child row
-- because of FOREIGN KEY constraint.