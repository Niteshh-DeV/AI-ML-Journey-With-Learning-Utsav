# Decision Trees in Supervised Learning

A decision tree is a non-parametric model that predicts a target by learning simple decision rules inferred from data features. It works for both classification and regression.

Key concepts
- Structure: internal nodes are tests on features, edges are outcomes of tests, leaves store predictions.
- Splitting: recursively partition data to make child nodes purer than parents.
- Criteria:
    - Classification: Gini impurity (1 − Σ p_i^2), Entropy (−Σ p_i log2 p_i), Information Gain.
    - Regression: variance reduction / mean squared error reduction.
- Handling features:
    - Numeric: threshold splits (e.g., x_j ≤ t).
    - Categorical: binary splits; some algorithms handle multiway splits; often one-hot encoding is used.
- Stopping conditions: max depth, min samples per split/leaf, no impurity improvement, or pure nodes.
- Pruning:
    - Pre-pruning: restrict growth via hyperparameters.
    - Post-pruning: cost-complexity pruning (ccp_alpha) to reduce overfitting.

Advantages
- Interpretable and easy to visualize.
- Handles nonlinear relationships and feature interactions.
- Minimal preprocessing; robust to outliers and monotonic transforms.
- Works with mixed feature types.
- Provides feature importance (impurity-based or permutation).

Limitations
- Prone to overfitting without regularization.
- High variance: small data changes can alter the tree.
- Axis-aligned splits may miss oblique boundaries.
- Bias toward features with many categories (for some criteria).
- Regression trees produce piecewise-constant predictions.

Common algorithms
- ID3 (entropy, multiway splits), C4.5 (handles continuous features, pruning), CART (Gini/MSE, binary splits). Ensembles like Random Forests and Gradient Boosted Trees address variance and bias trade-offs.

Practical tips
- Tune: max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes, ccp_alpha, class_weight (imbalanced classes).
- Validate with cross-validation; monitor accuracy/F1 (classification) or RMSE/MAE (regression).
- Handle missing values via imputation (e.g., median); some libraries (LightGBM, XGBoost) handle missing natively.
- Inspect feature importances and use permutation importance for reliable estimates.

Minimal example (scikit-learn)
- Classification:
    - from sklearn.tree import DecisionTreeClassifier
    - clf = DecisionTreeClassifier(max_depth=5, random_state=42)
    - clf.fit(X_train, y_train)
    - y_pred = clf.predict(X_test)
- Regression:
    - from sklearn.tree import DecisionTreeRegressor
    - reg = DecisionTreeRegressor(max_depth=5, random_state=42)
    - reg.fit(X_train, y_train)
    - y_pred = reg.predict(X_test)

Use cases
- Credit approval, churn prediction, medical triage, fraud detection, price prediction, and as base learners in tree ensembles.

Summary
- Decision trees partition feature space into regions with mostly single-class (classification) or similar target values (regression). With proper regularization or via ensembles, they offer strong accuracy while retaining interpretability.