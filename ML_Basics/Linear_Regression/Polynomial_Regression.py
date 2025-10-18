from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures # For generating polynomial features
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Sample data
np.random.seed(42)
X = np.linspace(0, 10, 50).reshape(-1, 1) # 50 data points from 0 to 10
Y = 2 + 1.5*X - 0.5*X**2 + np.random.randn(50, 1) * 2  # Quadratic relation with noise

# Generate polynomial features
poly = PolynomialFeatures(degree=2) # degree 2 for quadratic
X_poly = poly.fit_transform(X) # fit_transform to create polynomial features

# Split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(X_poly, Y, test_size=0.2, random_state=42)

# Train the model
model = LinearRegression()
model.fit(X_train, Y_train)

# Predict
Y_pred = model.predict(X_test)

# Evaluation Metrics

print("Mean Absolute Error:", mean_absolute_error(Y_test, Y_pred))
print("Mean Squared Error:", mean_squared_error(Y_test, Y_pred))
print("R^2 Score:", r2_score(Y_test, Y_pred))

# Visualize

plt.scatter(X, Y, color='blue', label='Data Points')
# Sort X for a smooth curve
X_sorted = np.sort(X, axis=0)
X_sorted_poly = poly.transform(X_sorted)
Y_sorted_pred = model.predict(X_sorted_poly)
plt.plot(X_sorted, Y_sorted_pred, color='red', label='Polynomial Regression Fit')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polynomial Regression - Degree 2')
plt.legend()
plt.show()

