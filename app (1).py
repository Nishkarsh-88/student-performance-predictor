import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("student_model.joblib")

st.title("🎓 Student Performance Predictor")
st.write("Enter student details and predict whether the student will **Pass or Fail**")

study_hours = st.slider("Study Hours per Day", 0.0, 10.0, 2.0)
attendance = st.slider("Attendance (%)", 0.0, 100.0, 75.0)
previous_scores = st.slider("Previous Exam Score", 0.0, 100.0, 65.0)

if st.button("Predict"):
    features = np.array([[study_hours, attendance, previous_scores]])
    result = model.predict(features)

    if result[0] == 1:
        st.success("✅ The student is likely to PASS.")
    else:
        st.error("❌ The student is likely to FAIL.")