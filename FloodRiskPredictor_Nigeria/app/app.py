import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.predictor import load_model, predict_flood_risk

# Load trained model
model = load_model('model/flood_model.pkl')

# Page config
st.set_page_config(page_title="Flood Risk Predictor", page_icon="🌧️", layout="centered")

# Styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton > button {
        background-color: #0e6ba8;
        color: white;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True
)

# Header
st.title("🌍 Nigerian State Flood Risk Predictor")
st.subheader("AI-powered prediction based on environmental conditions")
st.markdown("Use this tool to predict the **likelihood of flood risk** based on rainfall, elevation, slope, and vegetation index (NDVI).")

# Instructions section
with st.expander("ℹ️ How It Works"):
    st.markdown("""
    - Enter the environmental values using the sliders below.
    - The app uses a trained machine learning model to classify the flood risk.
    - Risk levels: **Low (🟢)**, **Moderate (🟠)**, **High (🔴)**
    """)

# Input form
st.markdown("---")
with st.form("flood_form"):
    st.markdown("### 🧪 Environmental Data Inputs")
    rainfall = st.slider("🌧️ Rainfall (mm)", 0, 300, 100)
    elevation = st.slider("⛰️ Elevation (m)", 0, 1000, 200)
    slope = st.slider("📐 Slope (degrees)", 0.0, 45.0, 5.0)
    ndvi = st.slider("🌿 NDVI (vegetation index)", 0.0, 1.0, 0.5)

    submitted = st.form_submit_button("🚀 Predict Flood Risk")

# Prediction output
if submitted:
    features = [rainfall, elevation, slope, ndvi]
    risk = predict_flood_risk(model, features)

    if risk == "Low":
        color = "🟢"
        message = "Low flood risk — minimal threat."
    elif risk == "Moderate":
        color = "🟠"
        message = "Moderate risk — stay alert and monitor."
    else:
        color = "🔴"
        message = "High flood risk — take preventive action!"

    st.markdown("---")
    st.markdown(f"### 🌊 Predicted Flood Risk: {color} **{risk}**")
    st.info(message)

# Footer
st.markdown("---")
st.caption("Made with ❤️ for Nigeria • Powered by Streamlit + AI")

