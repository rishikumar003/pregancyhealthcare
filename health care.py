import pandas as pd
import pickle
import streamlit as st
from sklearn.preprocessing import StandardScaler

# Load trained models
fetal_model = pickle.load(open("fetal_health_model.pkl", "rb"))
maternal_model = pickle.load(open("maternal_health_model.pkl", "rb"))

# Load scalers for data preprocessing
fetal_scaler = pickle.load(open("fetal_scaler.pkl", "rb"))
maternal_scaler = pickle.load(open("maternal_scaler.pkl", "rb"))

def main():
    st.title("Healthcare Risk Prediction")
    
    option = st.selectbox("Select Prediction Type", ["Fetal Health", "Maternal Health"])
    
    if option == "Fetal Health":
        st.header("Fetal Health Prediction")
        
        # User inputs
        features = []
        feature_names = ["baseline value", "accelerations", "fetal_movement", "uterine_contractions", "light_decelerations", "severe_decelerations", "prolongued_decelerations", "abnormal_short_term_variability", "mean_value_of_short_term_variability", "percentage_of_time_with_abnormal_long_term_variability", "mean_value_of_long_term_variability", "histogram_width", "histogram_min", "histogram_max", "histogram_number_of_peaks", "histogram_number_of_zeroes", "histogram_mode", "histogram_mean", "histogram_median", "histogram_variance", "histogram_tendency"]
        import pandas as pd
import pickle
import streamlit as st
from preprocessing_module import load_scalers

# Load trained models
fetal_model = pickle.load(open("fetal_health_model.pkl", "rb"))
maternal_model = pickle.load(open("maternal_health_model.pkl", "rb"))

# Load scalers from module
fetal_scaler, maternal_scaler = load_scalers("fetal_scaler.pkl", "maternal_scaler.pkl")

def main():
    st.title("Healthcare Risk Prediction")
    
    option = st.selectbox("Select Prediction Type", ["Fetal Health", "Maternal Health"])
    
    if option == "Fetal Health":
        st.header("Fetal Health Prediction")
        
        # User inputs
        features = []
        feature_names = ["baseline value", "accelerations", "fetal_movement", "uterine_contractions", "light_decelerations", "severe_decelerations", "prolongued_decelerations", "abnormal_short_term_variability", "mean_value_of_short_term_variability", "percentage_of_time_with_abnormal_long_term_variability", "mean_value_of_long_term_variability", "histogram_width", "histogram_min", "histogram_max", "histogram_number_of_peaks", "histogram_number_of_zeroes", "histogram_mode", "histogram_mean", "histogram_median", "histogram_variance", "histogram_tendency"]
        
        for feature in feature_names:
            value = st.number_input(f"{feature}", value=0.0)
            features.append(value)
        
        # Predict button
        if st.button("Predict Fetal Health"):
            features_scaled = fetal_scaler.transform([features])
            prediction = fetal_model.predict(features_scaled)[0]
            st.success(f"Predicted Fetal Health Risk Level: {prediction}")
    
    elif option == "Maternal Health":
        st.header("Maternal Health Prediction")
        
        # User inputs
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        systolic_bp = st.number_input("Systolic BP", value=120)
        diastolic_bp = st.number_input("Diastolic BP", value=80)
        bs = st.number_input("Blood Sugar Level", value=5.0)
        body_temp = st.number_input("Body Temperature", value=37.0)
        heart_rate = st.number_input("Heart Rate", value=75)
        
        # Prepare data for prediction
        maternal_features = [age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]
        
        # Predict button
        if st.button("Predict Maternal Health"):
            maternal_features_scaled = maternal_scaler.transform([maternal_features])
            prediction = maternal_model.predict(maternal_features_scaled)[0]
            st.success(f"Predicted Maternal Health Risk Level: {prediction}")

if __name__ == "__main__":
    main()
        for feature in feature_names:
            value = st.number_input(f"{feature}", value=0.0)
            features.append(value)
        
        # Predict button
        if st.button("Predict Fetal Health"):
            features_scaled = fetal_scaler.transform([features])
            prediction = fetal_model.predict(features_scaled)[0]
            st.success(f"Predicted Fetal Health Risk Level: {prediction}")
    
    elif option == "Maternal Health":
        st.header("Maternal Health Prediction")
        
        # User inputs
        age = st.number_input("Age", min_value=18, max_value=100, value=30)
        systolic_bp = st.number_input("Systolic BP", value=120)
        diastolic_bp = st.number_input("Diastolic BP", value=80)
        bs = st.number_input("Blood Sugar Level", value=5.0)
        body_temp = st.number_input("Body Temperature", value=37.0)
        heart_rate = st.number_input("Heart Rate", value=75)
        
        # Prepare data for prediction
        maternal_features = [age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]
        
        # Predict button
        if st.button("Predict Maternal Health"):
            maternal_features_scaled = maternal_scaler.transform([maternal_features])
            prediction = maternal_model.predict(maternal_features_scaled)[0]
            st.success(f"Predicted Maternal Health Risk Level: {prediction}")

if __name__ == "__main__":
    main()
