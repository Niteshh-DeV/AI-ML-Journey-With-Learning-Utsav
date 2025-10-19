# ------------------------------
#Logistic Regression — Student Pass Prediction
# ------------------------------

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# ------------------------------
# Dataset: Study Hours vs Pass/Fail
# ------------------------------
# Hours studied
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
# 0 = Fail, 1 = Pass
Y = np.array([0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

# ------------------------------
# Model Training
# ------------------------------
model = LogisticRegression()
model.fit(X, Y)

# ------------------------------
# Prediction & Probability
# ------------------------------
study_hours = np.array([[4.5], [6.5], [8]])
pred = model.predict(study_hours)
prob = model.predict_proba(study_hours)

for i, hr in enumerate(study_hours): 
    print(f"Study Hours: {hr[0]} --> Prediction: {'Pass' if pred[i]==1 else 'Fail'} | Probability of Passing: {prob[i][1]:.2f}")

# ------------------------------
# Visualization
# ------------------------------
X_range = np.linspace(0, 10, 100).reshape(-1, 1)
Y_prob = model.predict_proba(X_range)[:, 1]
# Predict_probs is used to get the probability of the positive class (passing) and [:, 1] gives that column.

plt.figure(figsize=(8,5))
plt.scatter(X, Y, color='blue', label='Actual Data')
plt.plot(X_range, Y_prob, color='red', label='Logistic Regression Curve')
plt.title("Student Pass Prediction using Logistic Regression")
plt.xlabel("Hours Studied")
plt.ylabel("Probability of Passing")
plt.legend()
plt.show()