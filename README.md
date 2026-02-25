# Databricks Retail Advanced Lakehouse

This project demonstrates a complete end-to-end Lakehouse architecture built entirely on Databricks following a professional Medallion Architecture (Bronze to Silver to Gold) used in real enterprise pipelines.

## Project Highlights

1. Synthetic retail dataset generation (reproducible with fixed random seed)
2. Bronze → Silver → Gold Lakehouse modeling
3. Delta tables for all layers
4. Dimensional modeling (star schema)
5. Customer RFM segmentation
6. Daily sales aggregation
7. ML demand forecasting using Spark ML (Linear Regression)

## Prerequisites

- **Databricks workspace** (Community Edition or higher)
- **Databricks Runtime 13.x+** with Spark ML pre-installed

## How to Run

Run the notebooks in order on a Databricks cluster:

1. `01_generate_synthetic_data.py` — generates all synthetic data into Bronze Delta tables
2. `02_bronze_ingestion.sql` — validates and previews the Bronze layer
3. `03_silver_transformations.sql` — cleanses, types, and enriches data into Silver tables
4. `04_gold_marts.sql` — creates dimensional model (dims + facts) in the Gold layer
5. `05_ml_demand_forecast.sql` — builds Customer RFM segmentation (`fact_customer_rfm`)
6. `06_ml_demand_forecast_model.py` — trains a Linear Regression demand forecast model and saves predictions to `fact_product_forecast_example`

## Medallion Layers

### Bronze (raw ingestion)

`bronze_products_raw`, `bronze_stores_raw`, `bronze_customers_raw`, `bronze_orders_raw`, `bronze_order_items_raw`

### Silver (cleaned & conformed)

`silver_products`, `silver_stores`, `silver_customers`, `silver_orders`, `silver_order_items`

### Gold (analytics-ready)

`dim_product`, `dim_store`, `dim_customer`, `fact_order_lines`, `fact_daily_sales`, `fact_customer_rfm`, `fact_product_forecast_example`

## Notebooks Breakdown

| Notebook | Type | Description |
|----------|------|-------------|
| `01_generate_synthetic_data.py` | Python | Generates synthetic retail data (Products, Stores, Customers, Orders, Order Items) and saves directly into Bronze Delta tables. Uses `random.seed(42)` for reproducibility. |
| `02_bronze_ingestion.sql` | SQL | Explores & validates the Bronze layer — preview data, count records, understand source-level structures. |
| `03_silver_transformations.sql` | SQL | Data cleansing, type casting, enrichment — normalizes strings, adds ingestion timestamps, extracts `order_date`, transforms into clean Silver tables. |
| `04_gold_marts.sql` | SQL | Creates analytics-ready Gold layer — `dim_product`, `dim_store`, `dim_customer`, `fact_order_lines`, `fact_daily_sales`. |
| `05_ml_demand_forecast.sql` | SQL | Builds Customer RFM segmentation (`fact_customer_rfm`) with Recency, Frequency, and Monetary scoring. |
| `06_ml_demand_forecast_model.py` | Python | Trains a Spark ML Linear Regression model for product-level daily demand forecasting. Saves predictions to `fact_product_forecast_example`. |
