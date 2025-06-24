import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load dataset
try:
    df = pd.read_csv("data/rainfall_data.csv")
except FileNotFoundError:
    raise FileNotFoundError("🚫 Could not find 'data/rainfall_data.csv'. Make sure it exists.")

# Check required columns
required_columns = ['rainfall_mm', 'elevation_m', 'slope_deg', 'ndvi', 'flood_risk']
missing = [col for col in required_columns if col not in df.columns]
if missing:
    raise ValueError(f"🚨 Missing columns in CSV: {missing}")

# Extract features and target
X = df[['rainfall_mm', 'elevation_m', 'slope_deg', 'ndvi']]
y = df['flood_risk']

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
print("\n📊 Model Performance:")
print(classification_report(
    y_test,
    model.predict(X_test),
    labels=[0, 1, 2],
    target_names=["Low", "Moderate", "High"]
))

# Save model
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/flood_model.pkl")
print("\n✅ Model trained and saved to model/flood_model.pkl")
