import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score

# ------------------------------
# Generate Non-Linear Data
# ------------------------------

np.random.seed(42)
X = np.linspace(0, 10, 50).reshape(-1, 1)
Y = 2 + 1.5*X - 0.5*X**2 + np.random.randn(50, 1) * 2  # quadratic relationship

# ------------------------------
# Linear Regression (Baseline)
# ------------------------------

linear_model = LinearRegression()
linear_model.fit(X, Y)
Y_pred_linear = linear_model.predict(X)

# ------------------------------
# Polynomial Regression (Degree 2)
# ------------------------------

poly_feat = PolynomialFeatures(degree=2)
X_poly = poly_feat.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, Y)
Y_pred_poly = poly_model.predict(X_poly)

# ------------------------------
# Polynomial Regression (Degree 10 – Overfitting Example)
# ------------------------------

poly_feat_high = PolynomialFeatures(degree=10)
X_poly_high = poly_feat_high.fit_transform(X)

poly_model_high = LinearRegression()
poly_model_high.fit(X_poly_high, Y)
Y_pred_high = poly_model_high.predict(X_poly_high)

# ------------------------------
# Evaluation
# ------------------------------

print("Linear Model R²:", r2_score(Y, Y_pred_linear))
print("Polynomial (deg 2) R²:", r2_score(Y, Y_pred_poly))
print("Polynomial (deg 10) R²:", r2_score(Y, Y_pred_high))

# ------------------------------
# Visualization
# ------------------------------

plt.figure(figsize=(10,6))
plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X, Y_pred_linear, color='red', label='Linear Fit')
plt.plot(X, Y_pred_poly, color='green', label='Polynomial (Degree 2)')
plt.plot(X, Y_pred_high, color='orange', linestyle='--', label='Polynomial (Degree 10)')
plt.title("Polynomial Regression: Overfitting & Underfitting")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.show()