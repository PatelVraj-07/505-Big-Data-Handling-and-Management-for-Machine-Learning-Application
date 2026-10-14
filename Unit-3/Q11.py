import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.DataFrame({
 "YearsExperience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
 "Salary": [25000, 30000, 35000, 40000, 45000,
 50000, 55000, 60000, 65000, 70000]
})

X = df[["YearsExperience"]]
y = df["Salary"]

X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("Slope (coefficient):", model.coef_[0])
print("Intercept:", model.intercept_)

y_pred = model.predict(X_test)

results = pd.DataFrame({
 "Actual Salary": y_test.values,
 "Predicted Salary": y_pred
})
print("\nPredictions:")
print(results)

print("\nMean Squared Error:", mean_squared_error(y_test, y_pred))
print("R-squared score:", r2_score(y_test, y_pred))

new_prediction = model.predict(pd.DataFrame({"YearsExperience": [6]}))
print("Predicted salary for 6 years:", new_prediction[0])