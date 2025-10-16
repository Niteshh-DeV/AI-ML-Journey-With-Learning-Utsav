import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Sample data
X = np.array([500, 700, 800, 1000, 1200, 1500]).reshape(-1, 1) # Area in sq ft 
# .reshape(-1, 1) to make it a 2D array

# Price
y = np.array([150, 200, 220, 260, 300, 350])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Visualize
plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price (in $1000s)')
plt.title('Linear Regression - House Price Prediction')
plt.show()


# Evaluation Matrics
# Evaluation matrics are used to measure the performance of a machine learning model.

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
# Mean Absolute Error (MAE) is the average of the absolute differences between the predicted and actual values.
# It gives an idea of how much the predictions deviate from the actual values on average.

print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
# Mean Squared Error (MSE) is the average of the squared differences between the predicted and actual values.
# It gives more weight to larger errors, making it sensitive to outliers.

print("R^2 Score:", r2_score(y_test, y_pred))
# R^2 Score (Coefficient of Determination) indicates the proportion of the variance in the dependent variable that is predictable from the independent variable(s).
# An R^2 score of 1 indicates perfect prediction, while a score of 0 indicates that the model does not explain any of the variance in the target variable.
# Negative values of R^2 indicate that the model performs worse than a horizontal line (mean of the target variable).
