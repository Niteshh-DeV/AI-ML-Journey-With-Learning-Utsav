# AdaBoost (Adaptive Boosting)

## Overview
AdaBoost is an ensemble learning algorithm that combines multiple weak learners to create a strong classifier. It was introduced by Yoav Freund and Robert Schapire in 1996.

## Key Concepts

### How It Works
1. **Initial Weights**: All training samples start with equal weights
2. **Iterative Training**: Train weak learners sequentially
3. **Weight Update**: Increase weights of misclassified samples
4. **Final Prediction**: Weighted vote of all weak learners

### Mathematical Foundation
- Each weak learner gets a weight (α) based on its accuracy
- Misclassified samples get higher weights for the next iteration
- Final prediction: sign(Σ αᵢ × hᵢ(x))

## Advantages
- Reduces bias and variance
- Less prone to overfitting (theoretically)
- No need for feature scaling
- Works well with decision stumps

## Disadvantages
- Sensitive to noisy data and outliers
- Slower training time compared to some algorithms
- Can overfit if too many iterations

## Common Use Cases
- Face detection (Viola-Jones algorithm)
- Text classification
- Object detection
- Medical diagnosis

## Implementation Example
```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier

# Create AdaBoost classifier
ada = AdaBoostClassifier(
    base_estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50,
    learning_rate=1.0
)

# Train the model
ada.fit(X_train, y_train)

# Make predictions
predictions = ada.predict(X_test)
```

## Parameters
- **n_estimators**: Number of weak learners
- **learning_rate**: Weight applied to each classifier
- **base_estimator**: The weak learner to use
