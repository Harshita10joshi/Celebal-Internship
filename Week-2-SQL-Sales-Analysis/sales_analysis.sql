# IMPORT INTO MYSQL
create database superstore_db;
use superstore_db;
show tables;
	
# RENAMING THE TABLE 
RENAME TABLE `sample - superstore` TO sample_superstore;

# EXPLORE DATASET 
# 1) VIEW TABLE STRUCTUR
describe sample_superstore;

# 2) VIEW ALL DATA TOP 10 ROWS
select * from sample_superstore limit 10;

# 3) COUNT ROWS
select count(*) as Total_rows from sample_superstore;

# FILTERING (WHERE)
select * from sample_superstore where sales>1000;
select * from sample_superstore where Region="West";
select * from sample_superstore where category="Furniture";
select * from sample_superstore where Sales>500;
select * from sample_superstore where region="West" and Sales>500;

# AGGREGATION 
select sum(sales) as total_sales from sample_superstore;
select avg(sales) as average_sales from sample_superstore;
select sum(quantity) as total_quantity from sample_superstore;
select max(profit) as maximum_profit from sample_superstore;

# GROUP BY
select region,sum(sales) as total_sales from sample_superstore group by region;
select category,sum(sales) as total_sales from sample_superstore group by category;
select category,avg(profit) as avg_profit from sample_superstore group by category;
select region,sum(quantity) as total_quantity from sample_superstore group by region;

# SORTING & LIMIT 
select "product name" , sum(sales) as total_sales from sample_superstore 
group by "product name" order by total_sales desc limit 10;
select "category" , sum(sales) as total_sales from sample_superstore 
group by "category" order by total_sales desc;
select "region" , sum(sales) as total_sales from sample_superstore 
group by "region" order by total_sales desc;

# BUSINESS USE CASE 
# 1) MONTHLY SALARY TREND
select date_format("order date","%Y-%m") as month, 
sum(sales) as total_sales from sample_superstore
group by month order by month;

# 2) TOP CUSTOMERS
select 'customer name', 
sum(sales) as total_spent from sample_superstore
group by 'customer name' order by total_spent desc limit 10;

# 3) DUPLICATE CHECK 
select 'order id', count(*) as cnt from sample_superstore
group by 'order id' having count(*) >1;

# DATA VALIDATION 
# 1) Check for null values
select * from sample_superstore where sales is null or profit is null or quantity is null;

# 2) Check duplicate product IDs
select "product ID", count(*) as duplicate_count from
sample_superstore group by "product ID" having count(*)>1;
