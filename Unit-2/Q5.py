import os
import sys

os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

from pyspark.sql import SparkSession

try:
    print("Starting Spark...", flush=True)

    spark = (
        SparkSession.builder
        .appName("DataFrameExample")
        .master("local[1]")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )

    print("Spark started successfully!", flush=True)

    data = [
        {"ID": 1, "Name": "Vraj", "Age": 21},
        {"ID": 2, "Name": "Krish", "Age": 22},
        {"ID": 3, "Name": "Shubh", "Age": 20}
    ]

    df = spark.createDataFrame(data)

    print("\nDataFrame Schema:", flush=True)
    df.printSchema()

    print("\nDataFrame Records:", flush=True)
    df.show()

except Exception as e:
    print("Error:", e, flush=True)

finally:
    if "spark" in locals():
        spark.stop()