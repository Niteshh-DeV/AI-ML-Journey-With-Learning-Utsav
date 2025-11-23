Loan Prediction Project Documentation

Project Overview

The goal of this project is to predict whether a loan will be approved for an applicant based on personal, financial, and loan-related information using machine learning models.

Objective
	•	Build a model that predicts loan approval (Approved or Not Approved).
	•	Compare multiple machine learning models to find the best-performing model.
	•	Enable manual input prediction for interactive testing.

Dataset

The dataset contains 12 columns:

Column Name	Description
Gender	Male/Female
Married	Applicant’s marital status (Yes/No)
Dependents	Number of dependents (0, 1, 2, 3+)
Education	Graduate or Not Graduate
Self_Employed	Self-employed (Yes/No)
ApplicantIncome	Applicant’s monthly income
CoapplicantIncome	Co-applicant’s monthly income
LoanAmount	Loan amount requested (in thousands)
Loan_Amount_Term	Loan repayment term (in months)
Credit_History	1 if the applicant has credit history, 0 otherwise
Property_Area	Property location (Urban, Semiurban, Rural)
Loan_Status	Loan approved (Y) or not approved (N)

Tools & Libraries
	•	Python 3.x
	•	JupyterLab
	•	Libraries: pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, joblib

Project Steps

Step 1: Data Exploration
	•	Load dataset and examine first rows.
	•	Check missing values and data types.
	•	Visualize Loan_Status distribution and relationships with numeric features.

Step 2: Data Preprocessing
	•	Fill missing values: LoanAmount (median), Loan_Amount_Term (mode), Credit_History (mode)
	•	Encode categorical features using LabelEncoder.
	•	Scale numeric features using StandardScaler.

Step 3: Train-Test Split
	•	Split dataset into training (80%) and testing (20%) sets.

Step 4: Model Training

Tested multiple models:
	1.	Logistic Regression
	2.	Decision Tree
	3.	K-Nearest Neighbors
	4.	Random Forest
	5.	Gradient Boosting
	6.	XGBoost

Step 5: Model Evaluation
	•	Calculated accuracy, confusion matrix, and classification report for each model.
	•	Visualized model performance comparison.
	•	Selected the best-performing model (highest accuracy).

Step 6: Save Best Model
	•	Save the best model using joblib for future predictions.

Step 7: Manual Input Prediction
	•	Function to input applicant details and predict Approved/Not Approved.

Example: Likely Rejected Applicant

Feature	Value
Gender	Female (0)
Married	No (0)
Dependents	3+ (3)
Education	Not Graduate (0)
Self_Employed	Yes (1)
Applicant Income	1500
Coapplicant Income	0
Loan Amount	600
Loan Amount Term	360
Credit History	No (0)
Property Area	Rural (0)

Prediction: Not Approved

Visualizations
	1.	Loan Status Distribution
	2.	Boxplots of numeric features vs Loan_Status
	3.	Model accuracy comparison

How to Run This Project
	1.	Install Python 3.x and JupyterLab.
	2.	Install required libraries:

pip install pandas numpy matplotlib seaborn scikit-learn xgboost joblib

	3.	Open JupyterLab and load the loan_prediction.ipynb notebook.
	4.	Run the notebook from start to finish.
	5.	To test manual predictions, run the manual_input_prediction(best_model, scaler) function and input applicant details when prompted.

Conclusion
	•	End-to-end machine learning workflow demonstrated.
	•	Best model selected based on accuracy.
	•	Manual input feature allows interactive testing.

Next Steps
	•	Hyperparameter tuning using GridSearchCV.
	•	Feature engineering for improved prediction.
	•	Deploy as a web app using Flask/Django/Streamlit.

Files
	•	loan_data.csv → Dataset
	•	Loan_Prediction_Project.ipynb → Notebook
	•	best_loan_model.pkl → Saved best model
