# Logistic Regression

## Overview
Logistic Regression is a supervised machine learning algorithm used for binary classification problems. Despite its name, it's a classification algorithm, not a regression algorithm.

## Concept
	•	Unlike Linear Regression (which predicts continuous values), Logistic Regression predicts categories.
	•	It uses the Sigmoid function (S-shaped curve) to map predictions between 0 and 1.

$$P(Y=1|X) = \frac{1}{1 + e^{-(b_0 + b_1X)}}$$
	•	If P > 0.5 → class 1 (Yes)
If P ≤ 0.5 → class 0 (No)

Example: Predict whether a student passes or fails based on study hours.

## Key Concepts

### Sigmoid Function
The core of logistic regression is the sigmoid (logistic) function:
```
σ(z) = 1 / (1 + e^(-z))
```
This function maps any real-valued number to a value between 0 and 1.

### Hypothesis
```
h(x) = σ(θ^T x) = 1 / (1 + e^(-θ^T x))
```
Where θ represents the parameters (weights) and x represents the features.

## How It Works
1. **Linear Combination**: Computes a weighted sum of input features
2. **Sigmoid Transformation**: Applies the sigmoid function to get probability
3. **Decision Boundary**: Classifies based on a threshold (typically 0.5)

## Cost Function
Uses log loss (binary cross-entropy):
```
J(θ) = -1/m Σ[y*log(h(x)) + (1-y)*log(1-h(x))]
```

## Applications
- Email spam detection
- Disease diagnosis
- Credit risk assessment
- Customer churn prediction

## Advantages
- Simple and efficient
- Provides probability scores
- Works well for linearly separable data
- Less prone to overfitting with low-dimensional data

## Limitations
- Assumes linear decision boundary
- Sensitive to outliers
- Requires feature scaling
- Not suitable for complex non-linear problems

## Implementation
Common libraries: scikit-learn, TensorFlow, PyTorch

```python
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```