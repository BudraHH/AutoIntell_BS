import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
import joblib  # Import joblib to save the scaler

def load_and_preprocess_data(file_path):
    # Load dataset
    df = pd.read_csv(file_path)

    # Feature Engineering - Approximate heuristic for coolant change prediction
    df['Km Left Before Coolant Change'] = (df['Coolant temp'] * -0.5) + (df['Coolant pressure'] * 10) + \
                                          (df['Engine rpm'] * 0.03) + (df['lub oil temp'] * -0.2) + \
                                          (df['Lub oil pressure'] * 5) + (df['Fuel pressure'] * 2)

    # Define features and target variable
    X = df[['Coolant temp', 'Coolant pressure', 'Engine rpm', 'lub oil temp', 'Lub oil pressure', 'Fuel pressure']]
    y = df['Km Left Before Coolant Change'].values

    # Scale features using Min-Max scaling
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Save the scaler using joblib
    joblib.dump(scaler, "../model_weights/scaler_coolant.pkl")

    # Reshape for LSTM input (samples, time steps, features)
    X_scaled = X_scaled.reshape(X_scaled.shape[0], X_scaled.shape[1], 1)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test, scaler
