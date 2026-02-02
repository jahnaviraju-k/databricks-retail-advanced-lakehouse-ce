# Databricks Retail Advanced Lakehouse 

This project demonstrates a complete end-to-end Lakehouse architecture built entirely on Databricks following a professional Medallion Architecture (Bronze to Silver to Gold) used in real enterprise pipelines.

Project Highlights:

1. Synthetic retail dataset generation

2. Bronze → Silver → Gold Lakehouse modeling

3. Delta tables for all layers

4. Dimensional modeling

5. Customer RFM segmentation

6. Daily sales aggregation

7. ML demand forecasting using Spark ML

# Medallion Layers

1. Bronze

bronze_products_raw, bronze_stores_raw, bronze_customers_raw, bronze_orders_raw, bronze_order_items_raw

2. Silver

silver_products, silver_stores, silver_customers, silver_orders, silver_order_items

3. Gold

dim_product, dim_store, dim_customer, fact_order_lines, fact_daily_sales, fact_customer_rfm, fact_product_forecast_example

# Notebooks Breakdown
1. 01_generate_synthetic_data: Generates synthetic retail data for Products, Stores, Customers, Orders and Order items where everything is saved directly into bronze Delta tables.

2. 02_bronze_ingestion: Explores & validates the bronze layer for previewing data, Count records, Understand source-level structures

3. 03_silver_transformations: Performs data cleansing, typing & enrichment normalizing strings, Cast types, Adding ingestion timestamps, Extracting order_date and transforms into clean, conformed silver tables.

4. 04_gold_marts: Creates analytics-ready gold layer for dim_product, dim_store, dim_customer, fact_order_lines, fact_daily_sales, fact_customer_rfm (Recency, Frequency, Monetary segmentation)

5. 05_ml_demand_forecast: Builds a simple demand forecasting model using Spark ML where Linear Regression and product-level daily sales forecasting saving predictions into fact_product_forecast_example
