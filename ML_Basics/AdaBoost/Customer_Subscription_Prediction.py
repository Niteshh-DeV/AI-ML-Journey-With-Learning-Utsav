# AdaBoost Classifier — Customer Subscription Prediction

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Sample Dataset

data = {
    'Age': [22, 25, 28, 35, 40, 30, 50, 45, 32, 26, 48, 33],
    'Monthly_Income': [20000, 25000, 30000, 45000, 50000, 40000, 60000, 55000, 38000, 26000, 58000, 42000],
    'Calls_with_Agents': [2, 3, 4, 6, 7, 5, 8, 7, 5, 3, 6, 4],
    'Satisfaction_Score': [6, 7, 8, 9, 10, 8, 9, 9, 8, 7, 10, 9],
    'Subscribed': [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1]
}

df = pd.DataFrame(data)
print(" Dataset:\n", df)

#  Features and Target

X = df[['Age', 'Monthly_Income', 'Calls_with_Agents', 'Satisfaction_Score']]
y = df['Subscribed']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#  Train AdaBoost Classifier

# Using Decision Stump as base learner
base_estimator = DecisionTreeClassifier(max_depth=1, random_state=42)

ada_model = AdaBoostClassifier(
    estimator=base_estimator,
    n_estimators=100,
    learning_rate=0.1,
    random_state=42
)

ada_model.fit(X_train, y_train)

#  Predictions

y_pred = ada_model.predict(X_test)

# Model Evaluation

acc = accuracy_score(y_test, y_pred)
print("\nAccuracy:", round(acc * 100, 2), "%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Purples', cbar=False)
plt.title("Confusion Matrix — AdaBoost Classifier")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Feature Importance Visualization
importances = ada_model.feature_importances_
features = X.columns

plt.figure(figsize=(7, 5))
plt.barh(features, importances, color='darkviolet')
plt.title("Feature Importance — AdaBoost", fontsize=14)
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

print("\nPrediction Summary:\n", summary)