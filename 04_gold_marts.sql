%sql
USE retail_advanced;

-- Dim tables
CREATE OR REPLACE TABLE dim_product AS
SELECT
  product_id,
  product_name,
  category,
  brand,
  unit_of_measure,
  active_flag
FROM silver_products;

CREATE OR REPLACE TABLE dim_store AS
SELECT
  store_id,
  store_name,
  city,
  state,
  country,
  store_type
FROM silver_stores;

CREATE OR REPLACE TABLE dim_customer AS
SELECT
  customer_id,
  first_name,
  last_name,
  email,
  city,
  state,
  country,
  join_date
FROM silver_customers;

-- Fact: Order lines joined with product & store
CREATE OR REPLACE TABLE fact_order_lines AS
SELECT
  oi.order_item_id,
  o.order_id,
  o.order_date,
  o.order_ts,
  o.customer_id,
  o.store_id,
  s.store_name,
  s.city,
  s.state,
  s.country,
  s.store_type,
  oi.product_id,
  p.product_name,
  p.category,
  p.brand,
  oi.quantity,
  oi.unit_price,
  oi.discount_amount,
  oi.net_amount,
  o.currency
FROM silver_order_items oi
JOIN silver_orders o
  ON oi.order_id = o.order_id
LEFT JOIN silver_products p
  ON oi.product_id = p.product_id
LEFT JOIN silver_stores s
  ON o.store_id = s.store_id;

-- Fact: Daily aggregated sales
CREATE OR REPLACE TABLE fact_daily_sales AS
SELECT
  order_date,
  store_id,
  store_name,
  city,
  state,
  country,
  store_type,
  product_id,
  product_name,
  category,
  brand,
  SUM(quantity) AS total_units,
  SUM(net_amount) AS total_net_sales
FROM fact_order_lines
GROUP BY
  order_date,
  store_id,
  store_name,
  city,
  state,
  country,
  store_type,
  product_id,
  product_name,
  category,
  brand;
