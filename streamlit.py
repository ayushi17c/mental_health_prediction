import streamlit as st
import pickle
import numpy as np

# Load model
with open("rf_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Mental Health Prediction in the Workplace")

age = st.slider('Age', 18, 65, 30)
family_history = st.selectbox('Family History of Mental Illness', ['Yes', 'No'])
remote_work = st.selectbox('Remote Work', ['Yes', 'No'])
benefits = st.selectbox('Does your employer provide mental health benefits?', ['Yes', 'No'])
care_options = st.selectbox('Does your employer provide care options?', ['Yes', 'No'])
anonymity = st.selectbox('Is anonymity protected for those seeking mental health treatment?', ['Yes', 'No'])
leave = st.selectbox('How easy is it to take medical leave for mental health?', ['Very easy', 'Somewhat easy', "Don't know", 'Somewhat difficult', 'Very difficult'])
gender = st.selectbox('Gender', ['male', 'female', 'other'])
no_employees = st.selectbox('Company Size', ['6-25', '26-100', '100-500', '500-1000', 'More than 1000', '1-5'])
work_interfere = st.selectbox('How often does your mental health interfere with your work?', ['Never', 'Rarely', 'Sometimes', 'Often'])

# Map inputs to model features
leave_map = {'Very easy':2, 'Somewhat easy':1, "Don't know":0, 'Somewhat difficult':-1, 'Very difficult':-2}
input_vector = [
    age,
    1 if family_history == 'Yes' else 0,
    1 if remote_work == 'Yes' else 0,
    1 if benefits == 'Yes' else 0,
    1 if care_options == 'Yes' else 0,
    1 if anonymity == 'Yes' else 0,
    leave_map[leave],
    1 if gender == 'male' else 0,
    1 if gender == 'female' else 0,
    1 if no_employees == '6-25' else 0,
    1 if no_employees == '26-100' else 0,
    1 if no_employees == '100-500' else 0,
    1 if no_employees == '500-1000' else 0,
    1 if no_employees == 'More than 1000' else 0,
    1 if no_employees == '1-5' else 0,
    1 if work_interfere == 'Rarely' else 0,
    1 if work_interfere == 'Sometimes' else 0,
    1 if work_interfere == 'Often' else 0
]

if st.button("Predict"):
    prediction = model.predict([input_vector])[0]
    st.write("Prediction:", "Likely to need treatment" if prediction == 1 else "Not likely to need treatment")