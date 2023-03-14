import streamlit as st

def calculate_wells_score(active_cancer, bedridden_surgery, calf_swelling, collateral_veins, entire_leg_swollen, localized_tenderness, pitting_edema, paralysis_paresis_immobilization, previously_documented_dvt, alternative_diagnosis):
    """
    Calculate the Wells' score based on the input data.
    """
    score = 0
    if active_cancer == "Yes":
        score += 1
    if bedridden_surgery == "Yes":
        score += 1
    if calf_swelling == "Yes":
        score += 1
    if collateral_veins == "Yes":
        score += 1
    if entire_leg_swollen == "Yes":
        score += 1
    if localized_tenderness == "Yes":
        score += 1
    if pitting_edema == "Yes":
        score += 1
    if paralysis_paresis_immobilization == "Yes":
        score += 1
    if previously_documented_dvt == "Yes":
        score += 1
    if alternative_diagnosis == "Yes":
        score -= 2
    return score

def get_risk_group(score):
    """
    Determine the risk group based on the Wells' score.
    """
    if score <= 0:
        return "Low/unlikely"
    elif score <= 2:
        return "Moderate"
    else:
        return "High/likely"

def get_prevalence(risk_group):
    """
    Determine the prevalence of DVT based on the risk group.
    """
    if risk_group == "Low/unlikely":
        return "5%"
    elif risk_group == "Moderate":
        return "17%"
    else:
        return "17-53%"

# Name conversion dictionary
name_conversion = {
    "Active cancer (treatment or palliation within 6 months)": "active_cancer",
    "Bedridden recently >3 days or major surgery within 12 weeks": "bedridden_surgery",
    "Calf swelling >3 cm compared to the other leg (measured 10 cm below tibial tuberosity)": "calf_swelling",
    "Collateral (nonvaricose) superficial veins present": "collateral_veins",
    "Entire leg swollen": "entire_leg_swollen",
    "Localized tenderness along the deep venous system": "localized_tenderness",
    "Pitting edema, confined to symptomatic leg": "pitting_edema",
    "Paralysis, paresis, or recent plaster immobilization of the lower extremity": "paralysis_paresis_immobilization",
    "Previously documented DVT": "previously_documented_dvt",
    "Alternative diagnosis to DVT as likely or more likely": "alternative_diagnosis"
}

st.title("Wells' Criteria for DVT")
st.markdown('---')

# Create input form
input_data = {}
i = 0
col1, col2 = st.columns(2)
for question, key in name_conversion.items():
    if i % 2:
        col = col1
    else:
        col = col2
    answer = col.radio(question, ("No", "Yes"), key=key)
    input_data[key] = answer
    i += 1

# Calculate Wells' score and display results
wells_score = calculate_wells_score(**input_data)
risk_group = get_risk_group(wells_score)
prevalence = get_prevalence(risk_group)

# Display the results.
st.markdown('---')
st.success(f'**Wells\' Score:** {wells_score}')
st.success(f'**Risk Group:** {risk_group}')
st.success(f'**Prevalence of DVT:** {prevalence}')
