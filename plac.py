import streamlit as st
import numpy as np
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_model():
    with open("student_lr_final_model.pkl", "rb") as file:
        model, scaler, le = pickle.load(file)
    return model, scaler, le


def preprocessing_data(data, scaler, le):
    data = data.copy()

    data["Extracurricular Activities"] = le.transform(
        [data["Extracurricular Activities"]]
    )[0]

    df = pd.DataFrame([data])
    df_transformed = scaler.transform(df)

    return df_transformed


def predict_data(data):
    model, scaler, le = load_model()
    processed_data = preprocessing_data(data, scaler, le)
    prediction = model.predict(processed_data)
    return prediction


def main():
    st.title("Student Performance Prediction")
    st.write("Enter your data to get the prediction for your performance")

    hours_studied = st.number_input(
        "Hours Studied",
        min_value=1,
        max_value=10,
        value=5
    )

    previous_scores = st.number_input(
        "Previous Scores",
        min_value=40,
        max_value=100,
        value=70
    )

    extracurricular_activities = st.selectbox(
        "Extracurricular Activities",
        ["Yes", "No"]
    )

    sleep_hours = st.number_input(
        "Sleep Hours",
        min_value=4,
        max_value=10,
        value=6
    )

    sample_question_papers_practiced = st.number_input(
        "Sample Question Papers Practiced",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("Submit"):
        user_data = {
            "Hours Studied": hours_studied,
            "Previous Scores": previous_scores,
            "Extracurricular Activities": extracurricular_activities,
            "Sleep Hours": sleep_hours,
            "Sample Question Papers Practiced": sample_question_papers_practiced
        }

        prediction = predict_data(user_data)

        st.success(
            f"Predicted Performance Index: {prediction[0]:.2f}"
        )


if __name__ == "__main__":
    main()