# Databricks Retail Advanced Lakehouse 

This project demonstrates a complete end-to-end Lakehouse architecture built entirely on Databricks Community Edition — without Unity Catalog, Workflows, or Delta Live Tables — while still following a professional Medallion Architecture (Bronze → Silver → Gold) used in real enterprise pipelines.

Project Highlights

Synthetic retail dataset generation
Bronze → Silver → Gold Lakehouse modeling
Delta tables for all layers
Dimensional modeling
Customer RFM segmentation
Daily sales aggregation
Basic ML demand forecasting using Spark ML
Fully runnable on Databricks Community Edition

Architecture
databricks-retail-advanced-lakehouse-ce/
│
├── 01_generate_synthetic_data
├── 02_bronze_ingestion
├── 03_silver_transformations
├── 04_gold_marts
└── 05_ml_demand_forecast

Medallion Layers

# Bronze

bronze_products_raw

bronze_stores_raw

bronze_customers_raw

bronze_orders_raw

bronze_order_items_raw

# Silver

silver_products

silver_stores

silver_customers

silver_orders

silver_order_items

# Gold

dim_product

dim_store

dim_customer

fact_order_lines

fact_daily_sales

fact_customer_rfm

fact_product_forecast_example

# Notebooks Breakdown
01_generate_synthetic_data

Generates synthetic retail data for:

Products

Stores

Customers

Orders

Order items

Everything is saved directly into bronze Delta tables.

02_bronze_ingestion

Explores & validates the bronze layer:

Preview data

Count records

Understand source-level structures

03_silver_transformations

Performs data cleansing, typing & enrichment:

Normalize strings

Cast types

Add ingestion timestamps

Extract order_date

Transforms into clean, conformed silver tables.

04_gold_marts

Creates analytics-ready gold layer:

dim_product, dim_store, dim_customer

fact_order_lines

fact_daily_sales

fact_customer_rfm (Recency, Frequency, Monetary segmentation)

05_ml_demand_forecast

Builds a simple demand forecasting model using Spark ML:

Linear Regression

Product-level daily sales forecasting

Saves predictions into fact_product_forecast_example
