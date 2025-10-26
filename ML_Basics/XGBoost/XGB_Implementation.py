from xgboost import XGBClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Simple XGBoost classification example


def main():
    # Load dataset
    data = load_breast_cancer()
    X, y = data.data, data.target
    feature_names = data.feature_names

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

    # Define model
    model = XGBClassifier(
        n_estimators=300,
        max_depth=4, # Increased depth for more complex patterns
        learning_rate=0.05,
        subsample=0.9, # Subsample for regularization
        colsample_bytree=0.9, # column subsample for regularization
        reg_lambda=1.0, # L2 regularization
        tree_method="hist", # Efficient tree construction
        n_jobs=-1, # Use all CPU cores
        eval_metric="logloss", # Evaluation metric
        random_state=42, 
    )

    # Train
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, y_pred, digits=4, target_names=data.target_names))

    # Top feature importances
    importances = model.feature_importances_
    top_idx = importances.argsort()[::-1][:10]
    print("Top 10 features by importance:")
    for rank, idx in enumerate(top_idx, 1):
        print(f"{rank:2d}. {feature_names[idx]:30s} {importances[idx]:.4f}")


if __name__ == "__main__":
    main()