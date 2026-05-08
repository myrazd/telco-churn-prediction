## App setup
# Import libraries
import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Page setup
st.set_page_config(
    page_title="Telco Churn Prediction",
    page_icon="📊",
    layout="wide"
)

# App title
st.title("Telco Customer Churn Prediction")
st.write(
    "This dashboard predicts customer churn risk and provides retention recommendations."
)

# Sidebar information
st.sidebar.header("About")

st.sidebar.write(
    """
    This Streamlit dashboard predicts customer churn risk using a trained LightGBM machine learning model.

    The project includes:
    - churn prediction
    - risk scoring
    - customer segmentation
    - retention recommendations
    """
)

# Add a short instruction box
st.info(
    "Enter customer details below, then click Predict Churn to estimate churn risk and receive a retention recommendation."
)

## Load model files
# Load saved model
model = joblib.load(
    "model/lightgbm_churn_model.pkl"
)

# Load feature column names
model_features = joblib.load(
    "model/model_features.pkl"
)

st.divider()

## Create Customer Input Form
# Customer input form
st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Female", "Male"])
    senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
    partner = st.selectbox("Partner", ["No", "Yes"])
    dependents = st.selectbox("Dependents", ["No", "Yes"])
    tenure_months = st.number_input("Tenure Months", min_value=0, max_value=72, value=12)

with col2:
    monthly_charges = st.number_input("Monthly Charges (MYR)", min_value=0.0, value=70.0)
    total_charges = st.number_input("Annual Total Charges (MYR)", min_value=0.0, value=840.0)
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
    payment_method = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

# Service information
st.header("Service Information")

col3, col4 = st.columns(2)

with col3:
    phone_service = st.selectbox("Phone Service", ["No", "Yes"])
    multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])

with col4:
    device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])

## Feature Engineering
# Create engineered features

# Average monthly customer value
avg_monthly_value_myr = (
    total_charges / tenure_months
    if tenure_months > 0
    else 0
)

# Count active services
service_count = sum([
    phone_service == "Yes",
    multiple_lines == "Yes",
    online_security == "Yes",
    online_backup == "Yes",
    device_protection == "Yes",
    tech_support == "Yes",
    streaming_tv == "Yes",
    streaming_movies == "Yes"
])

# Online services flag
has_online_services = int(
    online_security == "Yes"
    or online_backup == "Yes"
)

# Streaming services flag
has_streaming_services = int(
    streaming_tv == "Yes"
    or streaming_movies == "Yes"
)

# Tenure group
if tenure_months <= 12:
    tenure_group = "New Customer"

elif tenure_months <= 48:
    tenure_group = "Mid-Term Customer"

else:
    tenure_group = "Long-Term Customer"

# Monthly charges level
if monthly_charges < 40:
    monthly_charges_level = "Low"

elif monthly_charges < 80:
    monthly_charges_level = "Medium"

else:
    monthly_charges_level = "High"

## Build prediction dataframe
# Create input dataframe
input_data = pd.DataFrame({
    "Gender": [gender],
    "Senior_Citizen": [senior_citizen],
    "Partner": [partner],
    "Dependents": [dependents],
    "Tenure_Months": [tenure_months],
    "Phone_Service": [phone_service],
    "Multiple_Lines": [multiple_lines],
    "Internet_Service": [internet_service],
    "Online_Security": [online_security],
    "Online_Backup": [online_backup],
    "Device_Protection": [device_protection],
    "Tech_Support": [tech_support],
    "Streaming_TV": [streaming_tv],
    "Streaming_Movies": [streaming_movies],
    "Contract": [contract],
    "Paperless_Billing": [paperless_billing],
    "Payment_Method": [payment_method],
    "Monthly_Charges": [monthly_charges],
    "Total_Charges": [total_charges],
    "Avg_Monthly_Value_MYR": [avg_monthly_value_myr],
    "Service_Count": [service_count],
    "Has_Online_Services": [has_online_services],
    "Has_Streaming_Services": [has_streaming_services],
    "Tenure_Group": [tenure_group],
    "Monthly_Charges_Level": [monthly_charges_level]
})

# One-hot encode input data
input_encoded = pd.get_dummies(input_data)

# Align input columns with training columns
input_encoded = input_encoded.reindex(
    columns=model_features,
    fill_value=0
)

## Make Prediction
# Prediction button
if st.button("Predict Churn"):

    # Predict churn probability
    churn_probability = model.predict_proba(input_encoded)[0][1]

    # Apply tuned threshold
    threshold = 0.30
    churn_prediction = "Yes" if churn_probability >= threshold else "No"

    # Assign risk tier
    if churn_probability >= 0.70:
        risk_tier = "Critical Risk"
    elif churn_probability >= 0.50:
        risk_tier = "High Risk"
    elif churn_probability >= 0.30:
        risk_tier = "Medium Risk"
    else:
        risk_tier = "Low Risk"

        # Assign customer persona
    if (
        tenure_months <= 12
        and monthly_charges >= 70
    ):
        customer_persona = "New High-Value Customer"

    elif (
        contract == "Two year"
        and tenure_months >= 48
    ):
        customer_persona = "Loyal Long-Term Customer"

    elif (
        internet_service == "Fiber optic"
        and monthly_charges >= 80
    ):
        customer_persona = "High Usage Digital Customer"

    elif monthly_charges < 40:
        customer_persona = "Budget-Conscious Customer"

    else:
        customer_persona = "Standard Customer"

    # Assign recommended action
    if risk_tier == "Critical Risk":
        recommended_action = "Offer retention incentive immediately"
    elif risk_tier == "High Risk":
        recommended_action = "Target with retention campaign"
    elif risk_tier == "Medium Risk":
        recommended_action = "Monitor engagement and usage"
    else:
        recommended_action = "No immediate intervention needed"

    st.divider()
    st.subheader("Prediction Result")

    col_result1, col_result2, col_result3 = st.columns(3)

    with col_result1:
        st.metric(
            label="Churn Probability",
            value=f"{churn_probability:.1%}"
        )

    with col_result2:
        st.metric(
            label="Prediction",
            value=churn_prediction
        )

    with col_result3:
        st.metric(
            label="Risk Tier",
            value=risk_tier
        )

    # Display churn probability progress bar
    st.progress(churn_probability)

    st.caption(
        "The progress bar represents the predicted churn probability."
    )

    if churn_prediction == "Yes":
        st.error("Customer is likely to churn.")
    else:
        st.success("Customer is unlikely to churn.")

    st.write(f"**Recommended Action:** {recommended_action}")
    st.write(f"**Customer Persona:** {customer_persona}")
