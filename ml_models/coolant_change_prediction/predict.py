import numpy as np
import joblib
import tensorflow as tf

# Define custom metric if needed
from tensorflow.keras.metrics import MeanSquaredError



def predict_coolant_change(coolant_temp, coolant_pressure, engine_rpm, lub_oil_temp, lub_oil_pressure, fuel_pressure):
    # Load trained LSTM model with custom objects (if mse is a custom metric)
    lstm_model = tf.keras.models.load_model(
        "../model_weights/pred_coolantChange.h5",
        custom_objects={'mse': MeanSquaredError()}  # Adjust if mse is custom
    )

    # Load scaler
    scaler = joblib.load("../model_weights/scaler_coolant.pkl")
    # Create feature array
    input_features = np.array([[coolant_temp, coolant_pressure, engine_rpm, lub_oil_temp, lub_oil_pressure, fuel_pressure]])

    # Scale the features
    input_scaled = scaler.transform(input_features)

    # Reshape for LSTM input
    input_reshaped = input_scaled.reshape(1, input_scaled.shape[1], 1)

    # Predict kilometers left before coolant change
    predicted_km_left = lstm_model.predict(input_reshaped)[0][0]

    return {
        "predicted_km_left": float(predicted_km_left)
    }

# Example usage
# if __name__ == "__main__":
#     result = predict_coolant_change(85, 1.8, 2500, 90, 4, 2.5)
#     print(f"Predicted Km Left Before Coolant Change: {result['predicted_km_left']:.2f} km")
