import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

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

# Save trained model
joblib.dump(model, "student_model.joblib")
print("✅ Model trained and saved as student_model.joblib")