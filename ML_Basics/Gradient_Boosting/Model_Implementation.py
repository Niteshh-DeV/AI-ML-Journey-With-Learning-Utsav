from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
import pandas as pd

# Sample data
data = {
    'Area': [1500, 1800, 2400, 3000, 3500, 4000],
    'Rooms': [3, 4, 3, 5, 4, 5],
    'Location': [8, 9, 6, 10, 9, 10],
    'Age': [10, 5, 15, 3, 7, 2],
    'Price': [250000, 300000, 350000, 500000, 450000, 600000]
}

df = pd.DataFrame(data)

X = df[['Area', 'Rooms', 'Location', 'Age']]
y = df['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train Gradient Boosting Regressor
gb_model = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, random_state=42)
# learning_rate controls the contribution of each tree to the final model like boosting, for eg 0.1 means each tree contributes 10% to the final prediction
gb_model.fit(X_train, y_train)

# Predict
y_pred = gb_model.predict(X_test)

# Evaluate
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error:{mse:.2f}")
print("Predicted Prices:", y_pred)