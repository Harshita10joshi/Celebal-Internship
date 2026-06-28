USE ecommerce_sales;
-- ==========================================
-- Section C - Aggregation
-- ==========================================

-- Q13. Count the total number of orders

SELECT COUNT(*) AS total_orders
FROM `orders`;

-- Q14. Find the total revenue from all Delivered orders

SELECT SUM(total_amount) AS total_revenue
FROM `orders`
WHERE status = 'Delivered';

-- Q15. Calculate the average unit price of products in each category

SELECT category,
       AVG(unit_price) AS average_price
FROM products
GROUP BY category;

-- Q16. For each order status, find the count of orders
-- and total revenue. Sort by revenue (descending).

SELECT status,
       COUNT(order_id) AS total_orders,
       SUM(total_amount) AS total_revenue
FROM `orders`
GROUP BY status
ORDER BY total_revenue DESC;

-- Q17. Find the most expensive and cheapest product
-- in each category

SELECT category,
       MAX(unit_price) AS highest_price,
       MIN(unit_price) AS lowest_price
FROM products
GROUP BY category;

-- Q18. List product categories where average price > 2000

SELECT category,
       AVG(unit_price) AS average_price
FROM products
GROUP BY category
HAVING AVG(unit_price) > 2000;