# Loan Approval Prediction using Random Forest

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import seaborn as sns
import numpy as np

# Dataset Creation
data = {
    'Income': [35000, 45000, 60000, 20000, 120000, 85000, 30000, 40000, 100000, 50000],
    'Credit_Score': [650, 700, 720, 580, 800, 750, 600, 690, 770, 710],
    'Employment_Status': ['Employed', 'Employed', 'Self-Employed', 'Unemployed', 
                          'Employed', 'Self-Employed', 'Unemployed', 'Employed', 
                          'Employed', 'Self-Employed'],
    'Age': [25, 30, 35, 22, 45, 40, 28, 33, 50, 29],
    'Loan_Amount': [10000, 15000, 20000, 5000, 25000, 18000, 7000, 12000, 22000, 16000],
    'Approved': ['No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes']
}

df = pd.DataFrame(data)
print("Dataset Sample:\n", df.head())

#Encode Categorical Values

df['Employment_Status'] = df['Employment_Status'].map({'Unemployed': 0, 'Employed': 1, 'Self-Employed': 2})
df['Approved'] = df['Approved'].map({'No': 0, 'Yes': 1})

#Split Data into Features & Labels


X = df[['Income', 'Credit_Score', 'Employment_Status', 'Age', 'Loan_Amount']]
y = df['Approved']

# Train-Test Split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and Train Model

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#  Predictions

y_pred = model.predict(X_test)

# Evaluation

print(" Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

#Test with a New Applicant

new_applicant = pd.DataFrame({
    'Income': [75000],
    'Credit_Score': [740],
    'Employment_Status': [1],  # Employed
    'Age': [32],
    'Loan_Amount': [15000]
})

prediction = model.predict(new_applicant)[0]
import matplotlib.pyplot as plt

# Visualization of the dataset
plt.figure(figsize=(10, 6))
sns.countplot(x='Approved', data=df)
plt.title('Loan Approval Count')
plt.xlabel('Loan Approval Status')
plt.ylabel('Count')
plt.show()

# Feature Importance
importances = model.feature_importances_
features = X.columns
indices = np.argsort(importances)[::-1] # This sorts the indices of importances in descending order


plt.figure(figsize=(10, 6))
plt.title('Feature Importances')
plt.bar(range(X.shape[1]), importances[indices], align='center')
plt.xticks(range(X.shape[1]), features[indices], rotation=10)
plt.xlim([-1, X.shape[1]])
plt.show()

print("\n Loan Approval Prediction:", "Approved " if prediction == 1 else "Not Approved ")