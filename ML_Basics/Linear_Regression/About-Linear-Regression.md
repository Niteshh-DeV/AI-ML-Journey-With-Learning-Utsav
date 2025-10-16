# Linear Regression

## What it is
Linear regression is a supervised learning algorithm used to predict continuous numerical values (e.g., marks, price, salary) by learning the relationship between input features (X) and an output variable (y). The algorithm fits a linear equation to observed data and learns coefficients that minimize prediction error.

Formula:
y = m x + c  
Where:
- m → slope (weight)  
- c → intercept (bias)

The algorithm learns the best m and c that minimize the prediction error (commonly via minimizing mean squared error).

## Core idea and equation
- General model: y = β0 + β1x1 + β2x2 + ... + βn xn + ε  
    where β are coefficients (weights) and ε is an error term.
- Goal: find coefficients that minimize prediction error (commonly mean squared error).

## Loss and fitting
- Typical loss: Mean Squared Error (MSE) = (1/m) Σ(y_i − ŷ_i)^2  
- Common fitting methods: Ordinary Least Squares (OLS), gradient descent, closed-form normal equations.  
- Evaluation metrics: R² (coefficient of determination), RMSE, MAE.

## Key assumptions
- Linearity: relationship between predictors and target is linear.  
- Independence: residuals are independent.  
- Homoscedasticity: residuals have constant variance.  
- Normality: residuals are approximately normally distributed (mainly for inference).  
- No (or low) multicollinearity among predictors.

## Types / variants of linear regression
- Simple Linear Regression  
    - One predictor x, model y = β0 + β1x (or y = m x + c).  
- Multiple Linear Regression  
    - Multiple predictors (X₁, X₂, X₃, …), still linear in parameters.  
- Polynomial Regression  
    - Linear in parameters but uses polynomial terms (e.g., x^2, x^3) to model non-linear relationships.  
- Regularized Linear Models  
    - Ridge Regression (L2): penalizes sum of squared coefficients to reduce variance.  
    - Lasso Regression (L1): penalizes sum of absolute coefficients, can produce sparse models (feature selection).  
    - Elastic Net: combination of L1 and L2 penalties.  
- Bayesian Linear Regression  
    - Places priors on coefficients and computes posterior distributions for uncertainty estimates.  
- Robust Regression  
    - Methods (e.g., Huber loss, RANSAC) that reduce sensitivity to outliers.

## When to use
- Predict continuous outcomes.  
- When the relationship is approximately linear or can be made linear by feature transforms.  
- As a baseline model due to simplicity and interpretability.

## Practical notes
- Inspect residual plots to validate assumptions.  
- Standardize or normalize features before regularized training.  
- Use feature selection or regularization when many correlated predictors exist.  
- Interpret coefficients carefully: they represent expected change in y per unit change in x, holding other features constant.

## Summary
Linear regression is a simple, interpretable foundation for regression tasks. Variants (polynomial, ridge, lasso, elastic net, Bayesian) extend it to handle nonlinearity, multicollinearity, overfitting, and uncertainty estimation.
