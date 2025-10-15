from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split # train test split is used to split the dataset into training and testing sets
from sklearn.linear_model import LogisticRegression # Logistic Regression model is used for classification tasks
from sklearn.metrics import accuracy_score # accuracy_score is used to evaluate the model's performance

# Load dataset
iris = load_iris()
print(type(iris)) # iris is a Bunch object, similar to a dictionary
print(iris.keys()) # keys of the Bunch object
print(iris.data[:5]) # first 5 rows of the feature data
print("target lables :",iris.target) # target labels
X, y = iris.data, iris.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# test_size=0.2 means 20% of the data will be used for testing and 80% for training
# random_state=42 ensures reproducibility of the results

# Train model
model = LogisticRegression(max_iter=200) # max_iter=200 increases the maximum number of iterations for convergence
# here we are using Logistic Regression for multi-class classification
model.fit(X_train, y_train)
# fit() method is used to train the model on the training data

# Evaluate
pred = model.predict(X_test) # predict() method is used to make predictions on the test data
print("Accuracy:", accuracy_score(y_test, pred)) 

# This code demonstrates a complete workflow of loading a dataset, splitting it into training and testing sets, training a machine learning model, and evaluating its performance.
# Accuracy score is the ratio of correctly predicted instances to the total instances in the test set.
# In this case, we are using the Iris dataset, which is a classic dataset for multi-class classification tasks.
# The Logistic Regression model is suitable for this task as it can handle multiple classes.
# The accuracy score will give us an idea of how well our model is performing on unseen data. 
# here our accuracy is 1.0 which means our model is performing very well on the test data.
