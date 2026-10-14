import pandas as pd
import numpy as np

data = {
 "Name": ["Vraj", "Krish", "Shubh", "Vatsal"],
 "Age": [20, np.nan, 19, np.nan],
 "Marks": [85, 78, np.nan, 78]
}
df = pd.DataFrame(data)
print("Original data:")
print(df)
print("\nMissing values in each column:")
print(df.isna().sum())

dropped_df = df.dropna()
print("\nAfter dropna():")
print(dropped_df)

mean_df = df.copy()
mean_df["Age"] = mean_df["Age"].fillna(mean_df["Age"].mean())
mean_df["Marks"] = mean_df["Marks"].fillna(mean_df["Marks"].mean())
print("\nAfter filling missing values with mean:")
print(mean_df)

median_df = df.copy()
median_df["Age"] = median_df["Age"].fillna(median_df["Age"].median())
median_df["Marks"] = median_df["Marks"].fillna(median_df["Marks"].median())

clean_df = mean_df.drop_duplicates()
print("\nAfter drop_duplicates():")
print(clean_df)

clean_df = clean_df.rename(columns={"Name": "Student_Name", "Marks": "Score"})

print("\nAfter renaming columns:")
print(clean_df)