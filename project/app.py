import streamlit as st
import pandas as pd
import joblib
import os

# ===============================
# Page Configuration
# ===============================
st.set_page_config(
    page_title="Social Assistance Eligibility Predictor",
    page_icon="🏛️",
    layout="centered"
)

st.title("🏛️ Social Assistance Eligibility Predictor")
st.markdown("""
This Decision Support System (DSS) estimates the probability of
household eligibility for social assistance using a Logistic Regression model.
""")

st.divider()

# ===============================
# Sidebar Input
# ===============================
st.sidebar.header("📊 Household Profile Input")

income = st.sidebar.number_input(
    "Monthly Income (IDR)",
    min_value=0,
    value=750000,
    step=50000
)

dependents = st.sidebar.slider(
    "Number of Dependents",
    min_value=0,
    max_value=10,
    value=2
)

house_condition = st.sidebar.selectbox(
    "House Condition",
    ["poor", "average", "good"]
)

# ===============================
# Load Model
# ===============================
MODEL_PATH = "project/regression/logit_model_bansos.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("Model file not found. Please run the notebook to generate the .pkl file.")
    st.stop()

model = joblib.load(MODEL_PATH)

# ===============================
# Encode Input (MATCH MODEL EXACTLY)
# ===============================

# Manual dummy encoding (drop_first=True → baseline = "poor")
house_avg = 1 if house_condition == "average" else 0
house_good = 1 if house_condition == "good" else 0

# Create full feature dictionary
input_dict = {
    "const": 1.0,
    "monthly_income": income,
    "num_dependents": dependents,
    "house_condition_average": house_avg,
    "house_condition_good": house_good
}

# Create DataFrame using EXACT model column order
input_data = pd.DataFrame([[input_dict[col] for col in model.model.exog_names]],
                          columns=model.model.exog_names)

# ===============================
# Predict
# ===============================
probability = model.predict(input_data)[0]

st.subheader("🔍 Predictive Analysis Result")

col1, col2 = st.columns(2)

with col1:
    st.metric("Eligibility Probability", f"{probability:.50%}")

with col2:
    if probability >= 0.16:
        st.success("Verdict: ELIGIBLE")
    else:
        st.error("Verdict: NOT ELIGIBLE")

st.divider()

st.info("""
Methodological Note:
The model was trained using Maximum Likelihood Estimation (MLE)
on 5,000 simulated household observations.
""")

st.caption("Developed for Econometrics & IT Scholarship Portfolio | 2026")
