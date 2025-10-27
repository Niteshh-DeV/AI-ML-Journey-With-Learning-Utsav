import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import AdaBoostClassifier

class AdaBoost:
    def __init__(self, n_estimators=50):
        """
        Initialize AdaBoost classifier
        
        Parameters:
        n_estimators: Number of weak learners to train
        """
        self.n_estimators = n_estimators
        self.estimators = []
        self.estimator_weights = []
    
    def fit(self, X, y):
        """
        Train the AdaBoost classifier
        
        Parameters:
        X: Training features
        y: Training labels (should be -1 or 1)
        """
        n_samples = X.shape[0]
        
        # Initialize weights uniformly
        weights = np.ones(n_samples) / n_samples
        
        for _ in range(self.n_estimators):
            # Train weak learner
            weak_learner = DecisionTreeClassifier(max_depth=1, random_state=42)
            weak_learner.fit(X, y, sample_weight=weights)
            
            # Make predictions
            predictions = weak_learner.predict(X)
            
            # Calculate error
            incorrect = (predictions != y)
            error = np.sum(weights * incorrect) / np.sum(weights)
            
            # Avoid division by zero
            error = np.clip(error, 1e-10, 1 - 1e-10)
            
            # Calculate estimator weight (alpha)
            alpha = 0.5 * np.log((1 - error) / error)
            
            # Update sample weights
            weights *= np.exp(-alpha * y * predictions)
            weights /= np.sum(weights)  # Normalize
            
            # Store the weak learner and its weight
            self.estimators.append(weak_learner)
            self.estimator_weights.append(alpha)
    
    def predict(self, X):
        """
        Make predictions using the trained AdaBoost classifier
        
        Parameters:
        X: Test features
        
        Returns:
        Predicted labels
        """
        # Get predictions from all weak learners
        estimator_predictions = np.array([
            estimator.predict(X) for estimator in self.estimators
        ])
        
        # Weighted vote
        weighted_predictions = np.dot(self.estimator_weights, estimator_predictions)
        
        # Return sign of weighted sum
        return np.sign(weighted_predictions)


# Example usage
if __name__ == "__main__":
    # Generate synthetic dataset
    X, y = make_classification(n_samples=1000, n_features=20, n_informative=15,
                               n_redundant=5, random_state=42)
    
    # Convert labels to -1 and 1
    y = np.where(y == 0, -1, 1)
    
    # Split dataset
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Train AdaBoost
    ada = AdaBoost(n_estimators=50)
    ada.fit(X_train, y_train)
    
    # Make predictions
    y_pred = ada.predict(X_test)
    
    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)
    print(f"AdaBoost Accuracy: {accuracy:.4f}")
    
    # Compare with sklearn's AdaBoost
    sklearn_ada = AdaBoostClassifier(n_estimators=50, random_state=42)
    sklearn_ada.fit(X_train, y_train)
    sklearn_pred = sklearn_ada.predict(X_test)
    sklearn_accuracy = accuracy_score(y_test, sklearn_pred)
    print(f"Sklearn AdaBoost Accuracy: {sklearn_accuracy:.4f}")