import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.DataFrame({
 "Age": [20, 25, 30, 35, 40, 45],
 "Salary": [25000, 30000, 40000, 50000, 60000, 70000],
 "Experience": [1, 2, 4, 5, 7, 9]
})

X = df[["Age", "Salary", "Experience"]]
y = [0, 0, 0, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
 X, y, test_size=0.2, random_state=42
)

standard_scaler = StandardScaler()
minmax_scaler = MinMaxScaler()

X_train_standard = standard_scaler.fit_transform(X_train)
X_test_standard = standard_scaler.transform(X_test)

X_train_minmax = minmax_scaler.fit_transform(X_train)
X_test_minmax = minmax_scaler.transform(X_test)

print("StandardScaler - training data:")
print(X_train_standard)

print("\nMinMaxScaler - training data:")
print(X_train_minmax)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))