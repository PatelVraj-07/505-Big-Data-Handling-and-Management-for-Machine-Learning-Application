import pandas as pd

df = pd.DataFrame({
 "Quantity": [10, 20, 30, 40, 50],
 "Price": [10.5, 20.2, 30.7, 40.1, 50.9],
 "City": ["Surat", "Mumbai", "Surat", "Pune", "Surat"]
})

def memory_mb(data):
 return data.memory_usage(deep=True).sum() / (1024 ** 2)
before = memory_mb(df)
print("Memory before optimization (MB):", round(before, 6))
print("\nOriginal data types:")
print(df.dtypes)

df["Quantity"] = pd.to_numeric(df["Quantity"], downcast="integer")
df["Price"] = pd.to_numeric(df["Price"], downcast="float")

df["City"] = df["City"].astype("category")
after = memory_mb(df)
print("\nOptimized data types:")
print(df.dtypes)
print("\nMemory after optimization (MB):", round(after, 6))

if before > 0:
 reduction = ((before - after) / before) * 100
 print("Memory reduction (%):", round(reduction, 2))
else:
 print("Memory reduction cannot be calculated.")