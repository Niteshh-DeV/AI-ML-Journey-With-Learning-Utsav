import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error, r2_score

# Sample Dataset

data = {
    'Area': [1500, 1800, 2400, 3000, 3500, 4000, 2800, 2200, 3200, 3700],
    'Rooms': [3, 4, 3, 5, 4, 5, 4, 3, 4, 5],
    'Location': [8, 9, 6, 10, 9, 10, 8, 7, 9, 10],
    'Age': [10, 5, 15, 3, 7, 2, 6, 12, 8, 4],
    'Price': [250000, 300000, 350000, 500000, 450000, 600000, 420000, 340000, 480000, 550000]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# Features and Target

X = df[['Area', 'Rooms', 'Location', 'Age']]
y = df['Price']

# Split data (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#  Model Training

gb_model = GradientBoostingRegressor(
    n_estimators=150,      # Number of trees
    learning_rate=0.1,     # Step size shrinkage
    max_depth=3,           # Depth of each tree
    random_state=42
)

gb_model.fit(X_train, y_train)

# Predictions

y_pred = gb_model.predict(X_test)

# Evaluation Metrics

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n Model Evaluation:")
print("Mean Squared Error (MSE):", round(mse, 2))
print("R² Score:", round(r2, 4))

# Visualization — Actual vs Predicted

plt.figure(figsize=(7, 5))
plt.scatter(y_test, y_pred, color='royalblue', s=80, edgecolors='k') # s is size of points
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linestyle='--', linewidth=2)
plt.title("Actual vs Predicted House Prices", fontsize=14)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.grid(True)
plt.show()

#  Feature Importance Visualization

importances = gb_model.feature_importances_
features = X.columns

plt.figure(figsize=(7, 5))
plt.barh(features, importances, color='seagreen')
plt.title("Feature Importance in Gradient Boosting", fontsize=14)
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.show()

# Residual Analysis

residuals = y_test - y_pred

plt.figure(figsize=(7, 5))
plt.scatter(y_pred, residuals, color='orange', s=80, edgecolors='k')
plt.axhline(0, color='red', linestyle='--')
plt.title("Residual Plot (Errors vs Predicted)", fontsize=14)
plt.xlabel("Predicted Price")
plt.ylabel("Residual (Actual - Predicted)")
plt.grid(True)
plt.show()

# Display Summary

summary = pd.DataFrame({
    'Actual Price': y_test.values,
    'Predicted Price': np.round(y_pred, 2),
    'Residual': np.round(residuals, 2)
})

print("\nPrediction Summary:\n", summary)