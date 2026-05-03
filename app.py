import streamlit as st

st.title("Liver Cirrhosis Stage Prediction")

# -----------------------------
# INPUTS
# -----------------------------
Ascites = st.selectbox("Ascites", ["N", "Y"])
Edema = st.selectbox("Edema", ["N", "Y"])

Bilirubin = st.number_input("Bilirubin", 0.0, 10.0, 0.6)
Albumin = st.number_input("Albumin", 1.0, 6.0, 4.5)

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("Predict Stage"):

    # ✅ CORRECT LOGIC
    if Bilirubin < 1.2 and Albumin > 4.0 and Ascites == "N" and Edema == "N":
        stage = "Stage 1 🟢 (Early)"

    elif 1.2 <= Bilirubin <= 3.0 and 3.0 <= Albumin <= 4.0:
        stage = "Stage 2 🟡 (Moderate)"

    else:
        stage = "Stage 3 🔴 (Severe)"

    st.success(stage)