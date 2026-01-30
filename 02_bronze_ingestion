%sql
USE retail_advanced;

-- Quick checks
SELECT * FROM bronze_products_raw LIMIT 5;
SELECT * FROM bronze_customers_raw LIMIT 5;
SELECT * FROM bronze_stores_raw LIMIT 5;
SELECT * FROM bronze_orders_raw LIMIT 5;
SELECT * FROM bronze_order_items_raw LIMIT 5;

-- Row counts
SELECT 'products' AS table_name, COUNT(*) AS cnt FROM bronze_products_raw
UNION ALL
SELECT 'customers', COUNT(*) FROM bronze_customers_raw
UNION ALL
SELECT 'stores', COUNT(*) FROM bronze_stores_raw
UNION ALL
SELECT 'orders', COUNT(*) FROM bronze_orders_raw
UNION ALL
SELECT 'order_items', COUNT(*) FROM bronze_order_items_raw;
