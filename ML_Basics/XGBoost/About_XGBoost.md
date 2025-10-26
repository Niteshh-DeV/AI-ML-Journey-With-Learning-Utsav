# XGBoost in Machine Learning

## Overview
XGBoost (Extreme Gradient Boosting) is a powerful and efficient implementation of gradient boosting framework for supervised learning. It's widely used in machine learning competitions and real-world applications.

## Key Features
- **Speed and Performance**: Highly optimized for computational speed and model performance
- **Regularization**: Built-in L1 (Lasso) and L2 (Ridge) regularization to prevent overfitting
- **Parallel Processing**: Supports parallel tree construction
- **Handling Missing Values**: Automatically learns the best direction for missing values
- **Tree Pruning**: Uses depth-first approach with max_depth parameter

## Algorithm
XGBoost uses gradient boosting, which combines weak learners (decision trees) sequentially to create a strong predictive model. Each new tree corrects errors made by previous trees.

## Common Parameters
- `learning_rate`: Step size shrinkage to prevent overfitting
- `max_depth`: Maximum depth of trees
- `n_estimators`: Number of boosting rounds
- `subsample`: Fraction of samples used for training each tree
- `colsample_bytree`: Fraction of features used for each tree

## Use Cases
- Classification problems
- Regression tasks
- Ranking problems
- Time series forecasting

## Installation
```python
pip install xgboost
```

## Basic Example
```python
import xgboost as xgb
from sklearn.model_selection import train_test_split

# Create DMatrix
dtrain = xgb.DMatrix(X_train, label=y_train)

# Set parameters
params = {'max_depth': 3, 'learning_rate': 0.1, 'objective': 'binary:logistic'}

# Train model
model = xgb.train(params, dtrain, num_boost_round=100)
```