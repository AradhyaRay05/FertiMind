import streamlit as st
import numpy as np
import pickle
import pandas as pd

with open(r'D:\Education\Coding\Machine Learning\Machine Learning Projects\Fertilizer Recommendation System\model.pkl', 'rb') as f:
    model = pickle.load(f)

with open(r'D:\Education\Coding\Machine Learning\Machine Learning Projects\Fertilizer Recommendation System\scaler.pkl', 'rb') as f:
    sc = pickle.load(f)

st.title("Fertilizer Prediction")


temperature_input = st.slider("Temparature", min_value=0)
humidity_input = st.slider("Humidity", min_value=0)
moisture_input = st.slider("Moisture", min_value=0)
soil_type_input = st.selectbox("Soil Type", ['Black', 'Clayey', 'Loamy', 'Red', 'Sandy'])
crop_type_input = st.selectbox("Crop Type", ['Cotton', 'Ground Nuts', 'Maize', 'Millets', 'Paddy', 'Pulses', 'Sugarcane', 'Tobacco', 'Wheat'])
nitrogen_input = st.slider("Nitrogen", min_value=0)
potassium_input = st.slider("Potassium", min_value=0)
phosphorous_input = st.slider("Phosphorous", min_value=0)

if st.button("Predict Fertilizer"):
    fert_dict = {
        1: 'Urea',
        2: 'DAP',
        3: '14-35-14',
        4: '28-28',
        5: '17-17-17',
        6: '20-20',
        7: '10-26-26'
    }

    soil_type_mapping = {'Black': 0, 'Clayey': 1, 'Loamy': 2, 'Red': 3, 'Sandy': 4}

    crop_type_mapping = {'Cotton': 1, 'Ground Nuts': 2, 'Maize': 3, 'Millets': 4, 'Paddy': 6, 'Pulses': 7, 'Sugarcane': 8, 'Tobacco': 9, 'Wheat': 10}

    soil_type_encoded = soil_type_mapping.get(soil_type_input, -1)
    crop_type_encoded = crop_type_mapping.get(crop_type_input, -1)
    features = [temperature_input, humidity_input, moisture_input, soil_type_encoded, crop_type_encoded, nitrogen_input, potassium_input, phosphorous_input]
    features_array = np.array(features).reshape(1, -1)
    scaled_features = sc.transform(features_array)
    prediction = model.predict(scaled_features)
    predicted_fertilizer_name = fert_dict.get(int(prediction[0]), "Unknown Fertilizer")
    st.write(f"The recommended fertilizer is: {predicted_fertilizer_name}")