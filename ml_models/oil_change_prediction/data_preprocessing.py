import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

def load_and_preprocess_data(filepath):
    # Load dataset
    df = pd.read_csv(filepath)

    # Define features and target
    features = ['Lub oil pressure', 'Engine rpm', 'Coolant pressure', 'lub oil temp', 'Coolant temp']
    target = 'Km Left Before Oil Change'

    # Creating the target variable based on heuristic estimation
    df[target] = (df['Lub oil pressure'] * 10) + (df['lub oil temp'] * -1) + \
                 (df['Engine rpm'] * 0.05) + (df['Coolant pressure'] * 3) + \
                 (df['Coolant temp'] * 0.3)

    # Extract features and target
    X = df[features].values
    y = df[target].values

    # Scale the features using MinMaxScaler
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X)

    # Reshape X for LSTM (samples, timesteps, features)
    X_scaled = X_scaled.reshape(X_scaled.shape[0], X_scaled.shape[1], 1)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

    return X_train, X_test, y_train, y_test
