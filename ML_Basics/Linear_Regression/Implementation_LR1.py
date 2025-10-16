import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Generate random dataset
np.random.seed(42) # Seed sets the random number generator for reproducibility

X = np.random.rand(50, 1) * 100   # 50 random points in range [0, 100)

Y = 3.5 * X + np.random.randn(50, 1) * 20 # Linear relation with noise

# Fit linear regression model
model = LinearRegression()
model.fit(X, Y)

# Predict values
Y_pred = model.predict(X)

plt.figure(figsize=(8,6)) 
plt.scatter(X, Y, color='blue', label='Data Points') 
plt.plot(X, Y_pred, color='red', linewidth=2, label='Regression Line') 
plt.title('Linear Regression on Random Dataset')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()