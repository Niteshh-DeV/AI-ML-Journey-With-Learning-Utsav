import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ------------------------------
# Create Dataset
# ------------------------------
data = {
    'Age': [22, 25, 47, 52, 46, 56, 55, 60, 62, 61],
    'Income': [25000, 40000, 80000, 110000, 85000, 150000, 140000, 130000, 120000, 125000],
    'Buy_Laptop': ['No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes']
}

df = pd.DataFrame(data)
print(" Sample Data:")
print(df.head())

# ------------------------------
# Prepare Data
# ------------------------------
X = df[['Age', 'Income']]
y = df['Buy_Laptop']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ------------------------------
# Train Model
# ------------------------------
model = DecisionTreeClassifier(criterion='entropy', random_state=42)
# cririon= 'entropy' for information gain
model.fit(X_train, y_train)

# ------------------------------
# Evaluation
# ------------------------------
y_pred = model.predict(X_test)
print("\n Model Evaluation:")
print(f"Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# ------------------------------
# Visualization of the Decision Tree
# ------------------------------
plt.figure(figsize=(10,6))
plot_tree(model, feature_names=['Age', 'Income'], class_names=['No', 'Yes'], filled=True)
plt.title("Decision Tree Visualization — Laptop Purchase Prediction")
plt.show()

# ------------------------------
# Predict New Case
# ------------------------------
new_person = pd.DataFrame({'Age': [30], 'Income': [70000]})
prediction = model.predict(new_person)[0]

print(f"\nNew Person (Age=30, Income=70000) --> Prediction: {'Will Buy ' if prediction == 'Yes' else 'Will Not Buy'}")