# 🌊 Flood Risk Predictor — Nigeria

An intelligent, offline-ready flood prediction tool built using **machine learning** and **geospatial data**. This project helps predict flood risk levels across Nigerian states based on real environmental indicators such as rainfall, elevation, land slope, and NDVI (vegetation index).

---

## 📌 Problem Statement

Flooding in Nigeria causes massive economic losses, agricultural disruption, and displacement every year — especially in flood-prone regions like Lagos, Bayelsa, and Benue.

Despite the risk, most communities lack **accessible tools** to predict or prepare for floods.

---

## 🛠️ Tools & Technologies

| Component | Tools Used |
|----------|------------|
| Programming | Python 3 |
| Machine Learning | Scikit-learn, Random Forest |
| Interface | Streamlit (Web App) |
| Geospatial Processing | Rasterio, GeoPandas, Folium |
| Visualization | Seaborn, Matplotlib |
| Deployment | Offline (Runs Locally) |

---

## 🚀 Features

✅ Predicts **flood risk** (Low / Moderate / High)  
🌦 Accepts real-time environmental inputs  
🗺️ Shows visual insights from sample data  
📁 Supports GeoTIFF and GeoJSON (optional)  
💻 Works 100% **offline** after setup  
📊 Clean interface for judges, users & learners

---

## 📂 Project Structure

FloodRiskPredictor_Nigeria/
├── app/
│ └── app.py # Streamlit interface
├── data/
│ ├── rainfall_data.csv # Sample training data
│ ├── elevation_data.tif # GeoTIFF (elevation)
│ ├── landcover_data.tif # GeoTIFF (land cover)
│ └── rainfall.geojson # GeoJSON sample overlay
├── model/
│ ├── train_model.py # ML training script
│ ├── predictor.py # Model loader/predictor
│ └── flood_model.pkl # Trained model (auto-generated)
├── utils/
│ ├── processing.py # Data cleaning / scaling
│ └── visualization.py # Charts and maps
├── requirements.txt
└── README.md


---

## 🧪 How to Run

### Step 1: Install Requirements

```bash
pip install -r requirements.txt

Step 2: Train the Model (if not already trained)
python model/train_model.py
This saves flood_model.pkl to model/.

Step 3: Launch the Web App
streamlit run app/app.py
