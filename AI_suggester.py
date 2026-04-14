import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import matplotlib.pyplot as plt
import pickle
# Load dataset
df = pd.read_csv("MATPLOTdata.csv")
df["length"] = df["password"].apply(len)
# Features (inputs)
X = df[["length", "size"]]


Y=df["entropy"]
# Split data
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# Train model
model = RandomForestRegressor(n_estimators=200,max_depth=10)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
length = 13
size = 96
f=open("entropy_model.pkl",'wb')
pickle.dump(model,f)
# Predict entropy (scaled if your model was trained on scaled)
entropy = model.predict([[length, size]])[0]

print("Predicted Entropy:", round(entropy, 2))
comparison = pd.DataFrame({
    "Actual": y_test[:10].values,
    "Predicted": y_pred[:10]
})

print(comparison)
# Evaluation
print("MAE:", mean_absolute_error(y_test, y_pred))
print("R2 Score:", r2_score(y_test, y_pred))

# Model equation
print("Feature Importance:", model.feature_importances_)


import numpy as np

plt.figure()

# Scatter plot
plt.scatter(y_test, y_pred)

# Perfect prediction line (y = x)
min_val = min(min(y_test), min(y_pred))
max_val = max(max(y_test), max(y_pred))

plt.plot([min_val, max_val], [min_val, max_val])

plt.xlabel("Actual Entropy")
plt.ylabel("Predicted Entropy")
plt.title("Actual vs Predicted Entropy (Prediction Graph)")

plt.show()