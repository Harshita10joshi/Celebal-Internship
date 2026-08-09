-- ==========================================
-- E-COMMERCE ORDER ANALYTICS SYSTEM
-- DATABASE SETUP
-- ==========================================

CREATE DATABASE IF NOT EXISTS ecommerce_analytics;

USE ecommerce_analytics;


-- ==========================================
-- 1. CUSTOMERS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(150),
    city VARCHAR(100),
    signup_date DATE NOT NULL
);


-- ==========================================
-- 2. PRODUCTS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(200) NOT NULL,
    category VARCHAR(100) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);


-- ==========================================
-- 3. ORDERS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS orders (
    order_id INT PRIMARY KEY,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    status VARCHAR(30) NOT NULL,

    CONSTRAINT fk_orders_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);


-- ==========================================
-- 4. ORDER ITEMS TABLE
-- ==========================================

CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INT PRIMARY KEY,
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity INT NOT NULL,
    unit_price DECIMAL(10,2) NOT NULL,

    CONSTRAINT fk_items_order
        FOREIGN KEY (order_id)
        REFERENCES orders(order_id),

    CONSTRAINT fk_items_product
        FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);