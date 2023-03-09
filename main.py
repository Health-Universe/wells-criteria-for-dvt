import streamlit as st

# function to calculate Wells' Criteria score
def calculate_wells_criteria_score(clinical_features):
    
    wells_score = 0
    
    if clinical_features["clinical_symptoms"] == "Yes":
        wells_score += 3
        
    if clinical_features["alternative_diagnosis"] == "No":
        wells_score += 3
        
    if clinical_features["heart_rate"] >= 100:
        wells_score += 1
        
    if clinical_features["immobilization"] == "Yes":
        wells_score += 1
        
    if clinical_features["previous_dvt_pe"] == "Yes":
        wells_score += 1
        
    if clinical_features["hemoptysis"] == "Yes":
        wells_score -= 1
        
    if clinical_features["malignancy"] == "Yes":
        wells_score += 1
        
    if wells_score < 0:
        wells_score = 0
        
    return wells_score

st.title("Wells' Criteria for DVT Calculator")

clinical_symptoms = st.selectbox("Clinical symptoms of DVT?", ["Yes", "No"])
alternative_diagnosis = st.selectbox("Is an alternative diagnosis more likely than DVT?", ["Yes", "No"])
heart_rate = st.number_input("Heart rate (beats/minute)", value=60, min_value=0, max_value=300, step=1)
immobilization = st.selectbox("Immobilization or surgery in the previous 4 weeks?", ["Yes", "No"])
previous_dvt_pe = st.selectbox("Previous DVT or PE?", ["Yes", "No"])
hemoptysis = st.selectbox("Hemoptysis?", ["Yes", "No"])
malignancy = st.selectbox("Known active malignancy?", ["Yes", "No"])

clinical_features = {
    "clinical_symptoms": clinical_symptoms,
    "alternative_diagnosis": alternative_diagnosis,
    "heart_rate": heart_rate,
    "immobilization": immobilization,
    "previous_dvt_pe": previous_dvt_pe,
    "hemoptysis": hemoptysis,
    "malignancy": malignancy
}

wells_score = calculate_wells_criteria_score(clinical_features)

st.write("Wells' Criteria score:", wells_score)

