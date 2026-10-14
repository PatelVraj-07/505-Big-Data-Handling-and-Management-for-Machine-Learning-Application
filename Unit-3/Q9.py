import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.DataFrame({
 "Age": [20, None, 22, 21],
 "City": ["Surat", "Mumbai", "Surat", "Pune"],
 "Grade": ["Good", "Average", "Excellent", "Good"]
})

print("Original data:")

print(df)

imputer = SimpleImputer(strategy="mean")
df[["Age"]] = imputer.fit_transform(df[["Age"]])

label_encoder = LabelEncoder()
df["Grade_Encoded"] = label_encoder.fit_transform(df["Grade"])

one_hot = OneHotEncoder(sparse_output=False, handle_unknown="ignore")
city_encoded = one_hot.fit_transform(df[["City"]])
city_df = pd.DataFrame(
 city_encoded,
 columns=one_hot.get_feature_names_out(["City"]),
 index=df.index
)

result = pd.concat([df, city_df], axis=1)

print("\nAfter imputation and encoding:")
print(result)
print("\nLabel mapping:")
print(dict(zip(label_encoder.classes_,
 label_encoder.transform(label_encoder.classes_))))