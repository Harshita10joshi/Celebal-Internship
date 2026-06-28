-- ==========================================
-- Section B - Filtering & Optimization
-- ==========================================
USE ecommerce_sales;
show tables;
-- Q7. Retrieve all orders with status = 'Delivered'

SELECT *
FROM `orders`
WHERE status = 'Delivered';

-- Q8. Find all Electronics products with unit_price > 2000

SELECT *
FROM products
WHERE category = 'Electronics'
  AND unit_price > 2000;

-- Q9. List customers who joined in 2024 and belong to Maharashtra

SELECT *
FROM customers
WHERE join_date BETWEEN '2024-01-01' AND '2024-12-31'
  AND state = 'Maharashtra';

-- Q10. Find all orders placed between 2024-08-10 and 2024-08-25
-- excluding Cancelled orders

SELECT *
FROM `orders`
WHERE order_date BETWEEN '2024-08-10' AND '2024-08-25'
  AND status <> 'Cancelled';

-- ===========================================================
-- Q11.
-- Index: idx_orders_date
--
-- Purpose:
-- Speeds up queries that filter or sort using order_date.
--
-- Example query that benefits from this index:
-- ============================================================

SELECT *
FROM `orders`
WHERE order_date BETWEEN '2024-08-01' AND '2024-08-31';

-- ============================================================
-- Q12.
-- Query:
-- SELECT * FROM customers WHERE YEAR(join_date)=2024;
--
-- This query is NOT index-friendly because the YEAR()
-- function is applied to the indexed column, preventing
-- efficient index usage.
--
-- Index-friendly (SARGable) version:
-- ============================================================

SELECT *
FROM customers
WHERE join_date BETWEEN '2024-01-01' AND '2024-12-31';