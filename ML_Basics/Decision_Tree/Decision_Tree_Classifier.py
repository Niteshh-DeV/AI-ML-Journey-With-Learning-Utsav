from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd
from sklearn.tree import plot_tree
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import sklearn.datasets as sklearndatas

# Load dataset
data = sklearndatas.load_iris()
X = pd.DataFrame(data.data, columns=data.feature_names)
Y = pd.Series(data.target, name='target')
print("Dataset Sample:\n", X.head())
print("Target Sample:\n", Y.head())

# Split dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)
print("\nTraining set size:", X_train.shape)
print("Testing set size:", X_test.shape)

# Create Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)
model.fit(X_train, Y_train)
print("\nModel trained successfully.")

# Make predictions
Y_pred = model.predict(X_test)
print("\nPredictions on test set:\n", Y_pred)

# Evaluate the model
accuracy = accuracy_score(Y_test, Y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Feature Importance
feature_importances = pd.Series(model.feature_importances_, index=X.columns)
print("\nFeature Importances:\n", feature_importances.sort_values(ascending=False))

# Visualization
import matplotlib.pyplot as plt

# Plot Feature Importances
plt.figure(figsize=(10, 6))
feature_importances.sort_values(ascending=True).plot(kind='barh') # barh for horizontal bar plot
plt.title('Feature Importances in Decision Tree')
plt.xlabel('Importance')
plt.ylabel('Features')
plt.tight_layout()
plt.show()

# Plot Decision Tree
plt.figure(figsize=(20, 10))
plot_tree(model, 
          feature_names=data.feature_names,
          class_names=data.target_names,
          filled=True,
          rounded=True,
          fontsize=10)
plt.title('Decision Tree Visualization')
plt.tight_layout()
plt.show()

# Confusion Matrix

cm = confusion_matrix(Y_test, Y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=data.target_names)
disp.plot(cmap='Blues')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.show()