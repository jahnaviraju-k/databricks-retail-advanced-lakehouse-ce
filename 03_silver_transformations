%sql
USE retail_advanced;

-- Silver Customers
CREATE OR REPLACE TABLE silver_customers AS
SELECT
  customer_id,
  first_name,
  last_name,
  email,
  city,
  state,
  country,
  TO_DATE(join_date) AS join_date,
  current_timestamp() AS ingestion_ts
FROM bronze_customers_raw;

-- Silver Products
CREATE OR REPLACE TABLE silver_products AS
SELECT
  product_id,
  TRIM(product_name) AS product_name,
  UPPER(TRIM(category)) AS category,
  UPPER(TRIM(brand)) AS brand,
  unit_of_measure,
  active_flag,
  current_timestamp() AS ingestion_ts
FROM bronze_products_raw;

-- Silver Stores
CREATE OR REPLACE TABLE silver_stores AS
SELECT
  store_id,
  TRIM(store_name) AS store_name,
  TRIM(city) AS city,
  TRIM(state) AS state,
  UPPER(TRIM(country)) AS country,
  UPPER(TRIM(store_type)) AS store_type,
  current_timestamp() AS ingestion_ts
FROM bronze_stores_raw;

-- Silver Orders
CREATE OR REPLACE TABLE silver_orders AS
SELECT
  order_id,
  customer_id,
  store_id,
  TO_TIMESTAMP(order_ts) AS order_ts,
  CAST(order_net_amount AS DOUBLE) AS order_net_amount,
  currency,
  TO_DATE(order_ts) AS order_date,
  current_timestamp() AS ingestion_ts
FROM bronze_orders_raw;

-- Silver Order Items
CREATE OR REPLACE TABLE silver_order_items AS
SELECT
  order_item_id,
  order_id,
  product_id,
  CAST(quantity AS INT) AS quantity,
  CAST(unit_price AS DOUBLE) AS unit_price,
  CAST(discount_amount AS DOUBLE) AS discount_amount,
  CAST(net_amount AS DOUBLE) AS net_amount,
  current_timestamp() AS ingestion_ts
FROM bronze_order_items_raw;
