# CREDIT CARD FRAUD DETECTION USING MACHINE LEARNING
# Author : Sanyogita Sharma

# IMPORT LIBRARIES
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score

# LOAD DATASET
df = pd.read_csv("DATASET/creditcard.csv")

# Display Dataset Information
# Display First 5 Rows
print(df.head())

# Shape of Dataset
print("\nShape of Dataset:")
print(df.shape)

# Column Names
print("\nColumn Names:")
print(df.columns)

# Dataset Information
print("\nDataset Information:")
df.info()

# Check Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Count Fraud and Genuine Transactions
print("\nTransaction Count:")
print(df["Class"].value_counts())

# Visualize Transaction Count
df["Class"].value_counts().plot(kind="bar")

# Data Visualization
plt.title("Fraud vs Genuine Transactions")
plt.xlabel("Class")
plt.ylabel("Number of Transactions")

plt.show()

# Separate Features and Target
X = df.drop("Class", axis=1)
y = df["Class"]

print("\nFeatures Shape:", X.shape)
print("Target Shape:", y.shape)

# Split Dataset into Training and Testing Data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Data:", X_train.shape)
print("Testing Data:", X_test.shape)

# Apply SMOTE to Balance the Dataset
smote = SMOTE(random_state=42)

X_train_smote, y_train_smote = smote.fit_resample(
    X_train,
    y_train
)

print("\nAfter Applying SMOTE:")
print(y_train_smote.value_counts())

# Create Logistic Regression Model
model = LogisticRegression(max_iter=1000, random_state=42)
print("\nModel Created Successfully!")

# Train the Model
model.fit(X_train_smote, y_train_smote)

print("Model Training Completed Successfully!")

# Make Predictions
y_pred = model.predict(X_test)

print("\nPrediction Completed Successfully!")

# Evaluate Model Performance
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

# Classification Report
report = classification_report(y_test, y_pred)

print("\nClassification Report:")
print(report)

# ROC-AUC Score
roc = roc_auc_score(y_test, y_pred)

print("\nROC-AUC Score:", roc)

# Save Trained Model
joblib.dump(model, "MODEL/credit_card_fraud_model.pkl")
print("\nModel Saved Successfully!")