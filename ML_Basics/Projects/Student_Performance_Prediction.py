# ------------------------------
# Student Performance Prediction Project
# ------------------------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# ------------------------------
# Create a Sample Dataset
# ------------------------------

np.random.seed(42)

# Simulating data
study_hours = np.random.randint(1, 10, 50)
sleep_hours = np.random.randint(4, 9, 50)
subjects = np.random.randint(3, 8, 50)

# Logic: more study, better sleep, fewer subjects → more chance to pass
pass_prob = 0.3*study_hours + 0.2*sleep_hours - 0.1*subjects + np.random.randn(50) # noise
pass_fail = (pass_prob > np.median(pass_prob)).astype(int)  # 1 = Pass, 0 = Fail

data = pd.DataFrame({
    'Study_Hours': study_hours,
    'Sleep_Hours': sleep_hours,
    'Subjects': subjects,
    'Pass': pass_fail
})

print("Sample Data:")
print(data.head())

# ------------------------------
# Visualization
# ------------------------------
plt.figure(figsize=(8,5))
sns.scatterplot(x='Study_Hours', y='Sleep_Hours', hue='Pass', data=data, palette='coolwarm', s=80)
plt.title("Study vs Sleep Hours (Pass/Fail)")
plt.show()

# ------------------------------
# Train-Test Split
# ------------------------------
X = data[['Study_Hours', 'Sleep_Hours', 'Subjects']]
Y = data['Pass']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

# ------------------------------
# Model Training
# ------------------------------
model = LogisticRegression()
model.fit(X_train, Y_train)

# ------------------------------
#  Model Evaluation
# ------------------------------
Y_pred = model.predict(X_test)

print("\nModel Evaluation:")
print(f"Accuracy: {accuracy_score(Y_test, Y_pred)*100:.2f}%")
print("\nConfusion Matrix:\n", confusion_matrix(Y_test, Y_pred))
print("\nClassification Report:\n", classification_report(Y_test, Y_pred))

# ------------------------------
# Predict on New Data
# ------------------------------
new_student = pd.DataFrame({
    'Study_Hours': [6],
    'Sleep_Hours': [7],
    'Subjects': [5]
})
prediction = model.predict(new_student)[0]
prob = model.predict_proba(new_student)[0][1]

print(f"\nNew Student Data: {new_student.values.tolist()[0]}")
print(f"Predicted Result: {'Pass ' if prediction==1 else 'Fail'} (Probability of Passing: {prob:.2f})")

# ------------------------------
# Feature Importance Visualization
# ------------------------------
coef_df = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_[0]
})

plt.figure(figsize=(6,4))
sns.barplot(x='Feature', y='Coefficient', data=coef_df, palette='viridis')
plt.title("Feature Importance in Prediction")
plt.show()