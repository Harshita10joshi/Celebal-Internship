USE superstore_db;
SELECT * FROM superstore_raw;
desc superstore_raw;
DROP TABLE IF EXISTS orders;
CREATE TABLE customers (
    customer_id VARCHAR(30) PRIMARY KEY,
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    country VARCHAR(50),
    city VARCHAR(50),
    state VARCHAR(50),
    postal_code VARCHAR(20),
    region VARCHAR(30)
);
INSERT INTO customers (
    customer_id,
    customer_name,
    segment,
    country,
    city,
    state,
    postal_code,
    region
)
SELECT
    `Customer ID`,
    MIN(`Customer Name`),
    MIN(Segment),
    MIN(Country),
    MIN(City),
    MIN(State),
    MIN(`Postal Code`),
    MIN(Region)
FROM superstore_raw
GROUP BY `Customer ID`;
SELECT COUNT(*) FROM customers;
SELECT * FROM customers LIMIT 10;
CREATE TABLE products (
    product_id VARCHAR(30) PRIMARY KEY,
    product_name VARCHAR(200),
    category VARCHAR(50),
    sub_category VARCHAR(50)
);
INSERT INTO products (
    product_id,
    product_name,
    category,
    sub_category
)
SELECT
    `Product ID`,
    MIN(`Product Name`),
    MIN(Category),
    MIN(`Sub-Category`)
FROM superstore_raw
GROUP BY `Product ID`;
SELECT COUNT(*) FROM products;
CREATE TABLE orders (
    order_id VARCHAR(30),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(30),
    product_id VARCHAR(30),
    sales DECIMAL(10,2),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(10,2)
);
SELECT
    `Order Date`,
    `Ship Date`
FROM superstore_raw
LIMIT 5;
INSERT INTO orders (
    order_id,
    order_date,
    ship_date,
    ship_mode,
    customer_id,
    product_id,
    sales,
    quantity,
    discount,
    profit
)
SELECT
    `Order ID`,
    STR_TO_DATE(`Order Date`, '%m/%d/%Y'),
    STR_TO_DATE(`Ship Date`, '%m/%d/%Y'),
    `Ship Mode`,
    `Customer ID`,
    `Product ID`,
    Sales,
    Quantity,
    Discount,
    Profit
FROM superstore_raw;
SELECT COUNT(*) FROM orders;

# Find all orders whose sales are greater than the average sales of all orders.
SELECT * FROM orders WHERE sales >
( SELECT AVG(sales) FROM orders );

# Find the highest-value order placed by each customer.
WITH RankedOrders AS
( SELECT customer_id, order_id, sales, ROW_NUMBER() OVER( PARTITION BY customer_id 
ORDER BY sales DESC ) AS rn FROM orders )
SELECT customer_id, order_id, sales FROM RankedOrders WHERE rn = 1;

# Calculate the total sales of each customer.
WITH CustomerSales AS
( SELECT customer_id, SUM(sales) AS total_sales FROM orders GROUP BY customer_id )
SELECT * FROM CustomerSales;

# Show customer names along with their total sales.
WITH CustomerSales AS
( SELECT customer_id, SUM(sales) AS total_sales FROM orders GROUP BY customer_id )
SELECT c.customer_name, cs.total_sales FROM CustomerSales cs JOIN customers c
ON cs.customer_id = c.customer_id ORDER BY cs.total_sales DESC;

# Assign a unique row number based on sales (highest sales gets Row Number 1).
SELECT customer_id, sales, ROW_NUMBER() OVER(ORDER BY sales DESC) AS row_num FROM orders;

# Rank the orders based on sales.
SELECT customer_id, sales, RANK() OVER(ORDER BY sales DESC) AS sales_rank
FROM orders;

# Display each customer's total sales and their rank based on total sales.
WITH CustomerSales AS ( SELECT customer_id, SUM(sales) AS total_sales FROM orders
GROUP BY customer_id )
SELECT c.customer_name, cs.total_sales, RANK() OVER(ORDER BY cs.total_sales DESC) AS customer_rank
FROM CustomerSales cs JOIN customers c ON cs.customer_id = c.customer_id;

# Top 10 Customers
WITH CustomerSales AS
( SELECT customer_id, SUM(sales) AS total_sales FROM orders GROUP BY customer_id )
SELECT c.customer_name, cs.total_sales FROM CustomerSales cs JOIN customers c
ON cs.customer_id = c.customer_id ORDER BY cs.total_sales DESC LIMIT 10;

# Lowest 10 Customers
WITH CustomerSales AS
( SELECT customer_id, SUM(sales) AS total_sales FROM orders GROUP BY customer_id )
SELECT c.customer_name, cs.total_sales FROM CustomerSales cs JOIN customers c
ON cs.customer_id = c.customer_id ORDER BY cs.total_sales ASC LIMIT 10;

# Customers with Only One Order
SELECT customer_id, COUNT(DISTINCT order_id) AS total_orders FROM orders GROUP BY customer_id
HAVING COUNT(DISTINCT order_id) = 1;

# Customers with Above Average Total Sales
WITH CustomerSales AS
( SELECT customer_id, SUM(sales) AS total_sales FROM orders GROUP BY customer_id )
SELECT * FROM CustomerSales WHERE total_sales >
( SELECT AVG(total_sales) FROM CustomerSales );