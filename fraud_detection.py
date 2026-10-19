
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="FraudRadar | Transaction Intelligence",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- LOAD MODEL ----------------
MODEL_PATH = Path(__file__).with_name("fraud_detection_pipeline.pkl")

@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)

try:
    model = load_model()
except Exception as e:
    st.error(f"Could not load the trained model: {e}")
    st.info(
        "Keep fraud_detection_pipeline.pkl in the same folder "
        "as fraud_detection.py."
    )
    st.stop()

# ---------------- CUSTOM DESIGN ----------------
st.markdown("""
<style>
.stApp {
    background: #F4F7FB;
}
[data-testid="stHeader"] {
    background: rgba(244,247,251,0.95);
}
.block-container {
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}
.hero {
    background: linear-gradient(120deg, #101C35, #183C59);
    padding: 30px 34px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}
.hero h1 {
    color: white;
    font-size: 2.6rem;
    margin: 0;
    letter-spacing: -1px;
}
.hero p {
    color: #C6D7E8;
    margin: 8px 0 0 0;
    font-size: 1.05rem;
}
.eyebrow {
    color: #55D6BE;
    font-weight: 700;
    letter-spacing: 2px;
    font-size: 0.75rem;
    margin-bottom: 10px;
}
.panel {
    background: white;
    padding: 24px;
    border: 1px solid #E1E8F0;
    border-radius: 16px;
    margin-bottom: 18px;
}
.panel h3 {
    color: #17243B;
    margin-top: 0;
}
.small-note {
    color: #68778D;
    font-size: 0.88rem;
}
div.stButton > button {
    width: 100%;
    min-height: 3.2rem;
    background: #087F70;
    color: white;
    border: none;
    border-radius: 10px;
    font-weight: 700;
    font-size: 1rem;
}
div.stButton > button:hover {
    background: #06665B;
    color: white;
    border: none;
}
[data-testid="stMetric"] {
    background: white;
    padding: 16px;
    border: 1px solid #E1E8F0;
    border-radius: 13px;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.markdown("## 🛡️ FraudRadar")
    st.caption("TRANSACTION INTELLIGENCE")
    st.divider()
    st.markdown("### About the app")
    st.write(
        "FraudRadar uses a trained machine-learning model "
        "to classify transactions based on their details."
    )
    st.divider()
    st.markdown("**Model:** Logistic Regression")
    st.markdown("**Task:** Binary classification")
    st.markdown("**Status:** App ready")
    st.caption("Predictions are estimates, not proof of fraud.")

# ---------------- HEADER ----------------
st.markdown("""
<div class="hero">
    <div class="eyebrow">AI • FINANCIAL SECURITY</div>
    <h1>🛡️ FraudRadar</h1>
    <p>AI-Powered Transaction Intelligence</p>
</div>
""", unsafe_allow_html=True)

st.markdown("### Transaction analysis")
st.write(
    "Enter the transaction details below to evaluate "
    "whether the trained model flags it as potentially fraudulent."
)

# ---------------- TRANSACTION INPUTS ----------------
left, right = st.columns(2, gap="large")

with left:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("### 💳 Transaction details")
    transaction_type = st.selectbox(
        "Transaction type",
        ["PAYMENT", "TRANSFER", "CASH_OUT", "DEPOSIT"]
    )
    amount = st.number_input(
        "Transaction amount",
        min_value=0.0,
        value=1000.0,
        step=100.0
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("### 👤 Sender account")
    oldbalanceOrg = st.number_input(
        "Original balance",
        min_value=0.0,
        value=10000.0,
        step=500.0
    )
    newbalanceOrig = st.number_input(
        "Balance after transaction",
        min_value=0.0,
        value=9000.0,
        step=500.0
    )
    st.markdown("</div>", unsafe_allow_html=True)

with right:
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("### 🏦 Receiver account")
    oldbalanceDest = st.number_input(
        "Receiver's original balance",
        min_value=0.0,
        value=0.0,
        step=500.0
    )
    newbalanceDest = st.number_input(
        "Receiver's balance after transaction",
        min_value=0.0,
        value=0.0,
        step=500.0
    )
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown('<div class="panel">', unsafe_allow_html=True)
    st.markdown("### 📊 Transaction overview")
    st.metric("Transaction amount", f"{amount:,.2f}")
    st.metric(
        "Sender balance change",
        f"{oldbalanceOrg - newbalanceOrig:,.2f}"
    )
    st.markdown(
        '<p class="small-note">Check that the entered balances '
        'match the transaction you want to evaluate.</p>',
        unsafe_allow_html=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- PREDICTION ----------------
st.divider()

if st.button("🔍  Analyze transaction", use_container_width=True):
    # Derived features expected by the trained pipeline.
    balanceDiffOrig = oldbalanceOrg - newbalanceOrig
    balanceDiffDest = newbalanceDest - oldbalanceDest

    input_data = pd.DataFrame([{
        "type": transaction_type,
        "amount": amount,
        "oldbalanceOrg": oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig,
        "oldbalanceDest": oldbalanceDest,
        "newbalanceDest": newbalanceDest,
        "balanceDiffOrig": balanceDiffOrig,
        "balanceDiffDest": balanceDiffDest
    }])

    try:
        prediction = model.predict(input_data)[0]

        st.markdown("## Analysis result")

        if prediction == 1:
            st.error(
                "⚠️ Potential Fraud Detected\n\n"
                "The model classified this transaction as potentially "
                "fraudulent. Further investigation is recommended."
            )
        else:
            st.success(
                "✅ No Fraud Flagged\n\n"
                "The model classified this transaction as non-fraudulent. "
                "This does not guarantee that the transaction is safe."
            )

        with st.expander("View derived transaction features"):
            st.dataframe(input_data, use_container_width=True)

    except Exception as e:
        st.error(f"Prediction failed: {e}")

st.divider()
st.caption(
    "FraudRadar • Machine Learning Project • "
    "For educational and demonstration purposes"
)

   