import joblib
import numpy as np

def load_model(model_path='model/flood_model.pkl'):
    """
    Loads a trained model from the given path.
    """
    try:
        return joblib.load(model_path)
    except FileNotFoundError:
        raise FileNotFoundError(f"🚨 Model file not found at: {model_path}")

def predict_flood_risk(model, features):
    """
    Predicts flood risk from a list of features:
    [rainfall_mm, elevation_m, slope_deg, ndvi]
    
    Returns: "Low", "Moderate", or "High"
    """
    features = np.array(features).reshape(1, -1)
    prediction = model.predict(features)
    
    # Map numeric output to risk labels
    risk_labels = {
        0: "Low",
        1: "Moderate",
        2: "High"
    }
    return risk_labels.get(prediction[0], "Unknown")
