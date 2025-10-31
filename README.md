# 🎓 Student Performance Predictor

This project uses machine learning to predict whether a student is likely to **pass or fail** based on their study habits and academic history.

---

## 🔍 Problem Statement

Educational institutions want to identify students who are at risk of failing so they can provide timely support. This tool predicts student performance using a logistic regression model based on key features.

---

## 📁 Dataset

The dataset includes the following features:
- `StudyHours` — Number of hours studied
- `Attendance` — Attendance percentage
- `PreviousScores` — Scores in previous exams  
The target column is:
- `Pass` — Whether the student passed (1) or failed (0)

---

## 🤖 Machine Learning Model

- **Algorithm:** Logistic Regression
- **Why?** It's simple, interpretable, and effective for binary classification tasks like pass/fail prediction.

---

## 🛠️ Tools Used

- Python
- pandas
- scikit-learn
- GitHub

---

## 📈 Sample Output

```bash
Model Accuracy: 0.85

--- Predict Student Performance ---
Enter study hours: 5
Enter attendance percentage: 85
Enter previous exam score: 70
Prediction: The student is likely to PASS.
