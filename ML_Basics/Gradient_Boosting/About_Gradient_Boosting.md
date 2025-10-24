# Gradient Boosting Machine (GBM) in Machine Learning

## Overview
Gradient Boosting Machine (GBM) is a powerful ensemble learning algorithm that builds models sequentially, where each new model corrects the errors made by previous models. It combines weak learners (typically decision trees) to create a strong predictive model.

## How It Works

### Core Concept
1. **Sequential Learning**: Models are built one after another
2. **Error Correction**: Each new model focuses on correcting residual errors from previous models
3. **Gradient Descent**: Uses gradient descent optimization in function space

### Algorithm Steps
1. Initialize the model with a constant value
2. For each iteration:
    - Calculate the residuals (errors) from the current model
    - Fit a new weak learner to these residuals
    - Update the model by adding the new learner with a learning rate
3. Repeat until the specified number of iterations or convergence

## Key Parameters

- **n_estimators**: Number of boosting stages (trees)
- **learning_rate**: Shrinks the contribution of each tree
- **max_depth**: Maximum depth of individual trees
- **subsample**: Fraction of samples used for fitting trees
- **min_samples_split**: Minimum samples required to split a node

## Advantages

✅ High predictive accuracy  
✅ Handles mixed data types  
✅ Captures complex non-linear relationships  
✅ Built-in feature importance  
✅ Robust to outliers

## Disadvantages

❌ Computationally expensive  
❌ Prone to overfitting without proper tuning  
❌ Sequential nature limits parallelization  
❌ Sensitive to noisy data  
❌ Requires careful hyperparameter tuning

## Popular Implementations

- **XGBoost** (Extreme Gradient Boosting)
- **LightGBM** (Light Gradient Boosting Machine)
- **CatBoost** (Categorical Boosting)
- **scikit-learn GradientBoostingClassifier/Regressor**

## Use Cases

- Classification problems
- Regression tasks
- Ranking problems
- Feature engineering
- Kaggle competitions