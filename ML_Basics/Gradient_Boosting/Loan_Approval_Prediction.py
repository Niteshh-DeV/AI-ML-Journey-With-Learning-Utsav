#  Gradient Boosting Classifier — Loan Approval Prediction

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import seaborn as sns

# Sample Dataset

data = {
    'Income': [35000, 60000, 80000, 120000, 40000, 70000, 30000, 90000, 110000, 50000],
    'CreditScore': [650, 700, 800, 850, 600, 720, 580, 780, 810, 640],
    'EmploymentStatus': [1, 1, 1, 1, 0, 1, 0, 1, 1, 0],  # 1=Employed, 0=Unemployed
    'LoanAmount': [200000, 250000, 300000, 400000, 150000, 280000, 100000, 320000, 380000, 180000],
    'Age': [25, 30, 40, 35, 27, 29, 23, 33, 38, 26],
    'Approved': [0, 1, 1, 1, 0, 1, 0, 1, 1, 0]  # Target variable
}

df = pd.DataFrame(data)
print(" Dataset:\n", df)

# Features and Target

X = df[['Income', 'CreditScore', 'EmploymentStatus', 'LoanAmount', 'Age']]
y = df['Approved']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#  Train Gradient Boosting Classifier

gb_clf = GradientBoostingClassifier(
    n_estimators=120,
    learning_rate=0.1,
    max_depth=3,
    random_state=42
)
gb_clf.fit(X_train, y_train)

# Predictions

y_pred = gb_clf.predict(X_test)

#  Model Evaluation

acc = accuracy_score(y_test, y_pred)
print("\n Accuracy:", round(acc * 100, 2), "%")
print("\n Classification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Greens', cbar=False)
plt.title("Confusion Matrix — Loan Approval Prediction")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Feature Importance Visualization

importances = gb_clf.feature_importances_
features = X.columns

plt.figure(figsize=(7, 5))
plt.barh(features, importances, color='royalblue')
plt.title("Feature Importance in Gradient Boosting Classifier", fontsize=14)
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