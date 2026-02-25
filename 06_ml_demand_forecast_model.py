# Databricks notebook: 06_ml_demand_forecast_model
# Builds a simple demand forecasting model using Spark ML
# Linear Regression on product-level daily sales

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml import Pipeline

spark = SparkSession.builder.appName("demand_forecast").getOrCreate()
spark.sql("USE retail_advanced")

# --------------------------------------------------
# 1. Prepare training data from fact_daily_sales
# --------------------------------------------------
daily_sales = spark.table("fact_daily_sales")

# Extract numeric date features for the model
df = (
    daily_sales
    .withColumn("day_of_week", F.dayofweek("order_date"))
    .withColumn("day_of_month", F.dayofmonth("order_date"))
    .withColumn("month", F.month("order_date"))
    .withColumn("year", F.year("order_date"))
    .withColumn("week_of_year", F.weekofyear("order_date"))
)

# Index categorical columns
category_indexer = StringIndexer(inputCol="category", outputCol="category_idx", handleInvalid="keep")
store_indexer = StringIndexer(inputCol="store_id", outputCol="store_idx", handleInvalid="keep")
product_indexer = StringIndexer(inputCol="product_id", outputCol="product_idx", handleInvalid="keep")

# --------------------------------------------------
# 2. Assemble feature vector
# --------------------------------------------------
feature_cols = [
    "category_idx", "store_idx", "product_idx",
    "day_of_week", "day_of_month", "month", "year", "week_of_year"
]

assembler = VectorAssembler(inputCols=feature_cols, outputCol="features", handleInvalid="skip")

# --------------------------------------------------
# 3. Train Linear Regression model
# --------------------------------------------------
lr = LinearRegression(
    featuresCol="features",
    labelCol="total_units",
    predictionCol="predicted_units",
    maxIter=50,
    regParam=0.1,
    elasticNetParam=0.5
)

pipeline = Pipeline(stages=[category_indexer, store_indexer, product_indexer, assembler, lr])

# Train/test split
train_df, test_df = df.randomSplit([0.8, 0.2], seed=42)

print(f"Training rows: {train_df.count()}, Test rows: {test_df.count()}")

model = pipeline.fit(train_df)

# --------------------------------------------------
# 4. Evaluate the model
# --------------------------------------------------
predictions = model.transform(test_df)

evaluator_rmse = RegressionEvaluator(
    labelCol="total_units",
    predictionCol="predicted_units",
    metricName="rmse"
)
evaluator_r2 = RegressionEvaluator(
    labelCol="total_units",
    predictionCol="predicted_units",
    metricName="r2"
)

rmse = evaluator_rmse.evaluate(predictions)
r2 = evaluator_r2.evaluate(predictions)

print(f"RMSE: {rmse:.4f}")
print(f"R2:   {r2:.4f}")

# --------------------------------------------------
# 5. Save predictions to fact_product_forecast_example
# --------------------------------------------------
forecast_output = (
    predictions
    .select(
        "order_date",
        "store_id",
        "store_name",
        "product_id",
        "product_name",
        "category",
        "brand",
        "total_units",
        "predicted_units",
        "total_net_sales"
    )
)

forecast_output.write.mode("overwrite").format("delta").saveAsTable("fact_product_forecast_example")

print("Forecast results saved to fact_product_forecast_example")
