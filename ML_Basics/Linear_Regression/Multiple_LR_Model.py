# ------------------------------
#  Day 20: Multiple Linear Regression + Model Evaluation
# ------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# ------------------------------
#  Generate a Sample Dataset
# ------------------------------

np.random.seed(42)

# Features
area = np.random.randint(800, 3500, 50)         # in square feet.
bedrooms = np.random.randint(1, 5, 50)          # number of bedrooms
location_index = np.random.randint(1, 10, 50)   # arbitrary location score

# Target variable (price)
price = (area * 150) + (bedrooms * 10000) + (location_index * 5000) + np.random.randint(20000, 80000, 50)
# This formula assumes price depends on area, number of bedrooms, and location index with some noise.
# ie Multiple Linear Regression scenario.

# Create DataFrame
data = pd.DataFrame({
    'Area': area,
    'Bedrooms': bedrooms,
    'Location_Index': location_index,
    'Price': price
})

print("Sample Data:")
print(data.head())

# ------------------------------
# Data Visualization
# ------------------------------

plt.figure(figsize=(8, 5))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# ------------------------------
# Train-Test Split
# ------------------------------

X = data[['Area', 'Bedrooms', 'Location_Index']]
Y = data['Price']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# ------------------------------
# Model Training
# ------------------------------

model = LinearRegression()
model.fit(X_train, Y_train)

# ------------------------------
#Prediction
# ------------------------------

Y_pred = model.predict(X_test)

# ------------------------------
# Model Evaluation
# ------------------------------

mae = mean_absolute_error(Y_test, Y_pred)
mse = mean_squared_error(Y_test, Y_pred)
r2 = r2_score(Y_test, Y_pred)

print("\n Model Evaluation:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
# The Bigger the MAE, the worse the model's predictions are on average.
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R² Score: {r2:.4f}")
# Closer the R² score is to 1, the better the model explains the variance in the target variable.

# ------------------------------
# Visualize Actual vs Predicted
# ------------------------------

plt.figure(figsize=(8,5))
plt.scatter(Y_test, Y_pred, color='purple', alpha=0.7) 
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.grid(True)
plt.title("Actual vs Predicted House Prices")
plt.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'r--') # Diagonal line 
plt.show()

# ------------------------------
# Print Model Coefficients
# ------------------------------

coeff_df = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])
# Coefficients indicate the change in the target variable for a one-unit change in the feature, holding other features constant.
# model.coef_ gives the coefficients for each feature in the same order as X.columns.

print("\n Model Coefficients:")
print(coeff_df)

print(f"\n Intercept: {model.intercept_:.2f}")
# Intercept is the expected mean value of Y when all X=0.