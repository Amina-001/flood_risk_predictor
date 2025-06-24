import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def plot_feature_distribution(df):
    """
    Plots histograms of input features.
    """
    st.markdown("### 📊 Feature Distributions")
    fig, axes = plt.subplots(2, 2, figsize=(10, 6))
    features = ['rainfall_mm', 'elevation_m', 'slope_deg', 'ndvi']

    for i, ax in enumerate(axes.flatten()):
        sns.histplot(df[features[i]], bins=10, ax=ax, kde=True)
        ax.set_title(features[i])
    st.pyplot(fig)

def show_risk_by_state(df):
    """
    Show bar plot of flood risk counts by state.
    """
    st.markdown("### 🧭 Flood Risk per State")
    fig, ax = plt.subplots()
    sns.countplot(data=df, x="state", hue="flood_risk", palette="coolwarm", ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)
