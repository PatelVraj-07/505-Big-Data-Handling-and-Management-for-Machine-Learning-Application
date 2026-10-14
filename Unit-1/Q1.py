import pandas as pd

data = {
 "Name": ["Vraj", "Krish", "Shubh", "Vatsal", "Pavan"],
 "Age": [20, 21, 19, 22, 20],
 "City": ["Surat", "Mumbai", "Surat", "Pune", "Mumbai"],
 "Marks": [85, 78, 92, 67, 88]
}

df = pd.DataFrame(data)

df.to_csv("students.csv", index=False)

df = pd.read_csv("students.csv")

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())

print("\nDataset dimensions (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types and non-null values:")
df.info()

print("\nSummary statistics of numeric and categorical columns:")
print(df.describe(include="all"))