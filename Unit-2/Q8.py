from pyspark.sql import SparkSession

spark = (SparkSession.builder
 .appName("Practical8")
 .master("local[*]")
 .getOrCreate())

data = [
 (1, "Vraj", "IT", 65000),
 (2, "Krish", "HR", 50000),
 (3, "Shubh", "IT", 72000)
]

df = spark.createDataFrame(data, ["ID", "Name", "Department", "Salary"])
path = "employee_parquet"

df.write.mode("overwrite").parquet(path)

loaded_df = spark.read.parquet(path)
print("Reloaded schema:")

loaded_df.printSchema()
print("Reloaded data:")
loaded_df.show()

print("Original row count:", df.count())
print("Reloaded row count:", loaded_df.count())

spark.stop()