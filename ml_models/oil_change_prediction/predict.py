import tensorflow as tf
import numpy as np
from ml_models.oil_change_prediction.data_preprocessing import load_and_preprocess_data



# Function to predict kilometers left before oil change
def predict_oil_change(lub_oil_pressure, engine_rpm, coolant_pressure, lub_oil_temp, coolant_temp):
    # Load trained model
    model = tf.keras.models.load_model(
        "ml_models/model_weights/pred_oilChange.h5",
        custom_objects={"mse": tf.keras.losses.MeanSquaredError()}
    )

    # Define the input data for prediction
    new_data = np.array([[lub_oil_pressure, engine_rpm, coolant_pressure, lub_oil_temp, coolant_temp]])

    # Load dataset to get the scaler (this assumes your preprocessing function also returns the scaler)
    _, X_test, _, _ = load_and_preprocess_data('ml_models/datasets/engine_dataset.csv')  # Get scaler shape
    scaler_shape = X_test.shape[1]  # Get number of features

    # Reshape the data to match LSTM input format
    new_data = new_data.reshape(1, scaler_shape, 1)

    # Predict kilometers left before oil change
    predicted_km_left = model.predict(new_data)

    return predicted_km_left[0][0]


# Example usage of the function
# lub_oil_pressure = 3.5
# engine_rpm = 1000
# coolant_pressure = 2
# lub_oil_temp = 80
# coolant_temp = 85
#
# predicted_km_left = predict_oil_change(lub_oil_pressure, engine_rpm, coolant_pressure, lub_oil_temp, coolant_temp)
# print(f"Predicted Km Left Before Oil Change: {predicted_km_left:.2f} km")
