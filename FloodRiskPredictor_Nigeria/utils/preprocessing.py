import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def load_dataset(path="data/rainfall_data.csv"):
    """
    Loads the CSV and returns a DataFrame.
    """
    try:
        df = pd.read_csv(path)
        return df
    except FileNotFoundError:
        raise FileNotFoundError("❌ Could not find the dataset file.")

def preprocess_features(df):
    """
    Scales environmental features to [0, 1] range.
    Returns processed DataFrame.
    """
    features = ['rainfall_mm', 'elevation_m', 'slope_deg', 'ndvi']
    scaler = MinMaxScaler()
    df_scaled = df.copy()
    df_scaled[features] = scaler.fit_transform(df_scaled[features])
    return df_scaled
