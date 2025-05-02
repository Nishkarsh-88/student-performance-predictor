import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("student_performance.csv")

# Features and target
X = df[['StudyHours', 'Attendance', 'PreviousScores']]
y = df['Pass']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
predictions = model.predict(X_test)
print("Model Accuracy:", accuracy_score(y_test, predictions))

# User input
print("\n--- Predict Student Performance ---")
study_hours = float(input("Enter study hours: "))
attendance = float(input("Enter attendance percentage: "))
previous_scores = float(input("Enter previous exam score: "))

# Make prediction
result = model.predict([[study_hours, attendance, previous_scores]])
if result[0] == 1:
    print("Prediction: The student is likely to PASS.")
else:
    print("Prediction: The student is likely to FAIL.")
