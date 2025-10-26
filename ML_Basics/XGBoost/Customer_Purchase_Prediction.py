# XGBoost Classifier — Customer Purchase Prediction

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from xgboost import XGBClassifier

# Sample Dataset
data = {
    'Age': [22, 25, 28, 35, 40, 30, 50, 45, 32, 26, 48, 33],
    'Income': [25000, 32000, 40000, 55000, 62000, 45000, 80000, 70000, 48000, 31000, 75000, 50000],
    'Prev_Purchases': [0, 1, 2, 3, 5, 2, 6, 4, 3, 1, 5, 2],
    'Time_on_Website': [20, 25, 40, 60, 70, 55, 90, 80, 65, 30, 85, 50],
    'Ad_Clicks': [2, 3, 4, 7, 9, 6, 10, 8, 7, 3, 9, 6],
    'Purchased': [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
print(" Dataset:\n", df)

# Features and Target

X = df[['Age', 'Income', 'Prev_Purchases', 'Time_on_Website', 'Ad_Clicks']]
y = df['Purchased']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train XGBoost Classifier

xgb_model = XGBClassifier(
    n_estimators=150,
    learning_rate=0.1,
    max_depth=3,
    random_state=42,
    eval_metric='logloss'
)

xgb_model.fit(X_train, y_train)

#  Predictions

y_pred = xgb_model.predict(X_test)

#  Evaluation

acc = accuracy_score(y_test, y_pred)
print("\n Accuracy:", round(acc * 100, 2), "%")
print("\n Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title("Confusion Matrix — XGBoost Classifier")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Feature Importance Visualization

importances = xgb_model.feature_importances_
features = X.columns

# Ensure the importances are sorted by importance score
sorted_indices = np.argsort(importances)[::-1]
sorted_features = features[sorted_indices]
sorted_importances = importances[sorted_indices]

plt.figure(figsize=(7, 5))
plt.barh(sorted_features, sorted_importances, color='mediumseagreen')
plt.title("Feature Importance — XGBoost", fontsize=14)
plt.xlabel("Importance Score")
plt.ylabel("Features")
plt.grid(True, axis='x', linestyle='--', alpha=0.6)
plt.show()

# Prediction Summary

summary = pd.DataFrame({
    'Actual': y_test.values,
    'Predicted': y_pred,
    'Prediction_Status': np.where(y_test == y_pred, 'Correct', 'Wrong')
})

print("\n Prediction Summary:\n", summary)