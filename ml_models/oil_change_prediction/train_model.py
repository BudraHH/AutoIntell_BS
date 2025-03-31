import tensorflow as tf
from data_preprocessing import load_and_preprocess_data
from model_lstm import create_lstm_model

# Load dataset and preprocess
X_train, X_test, y_train, y_test = load_and_preprocess_data('../datasets/engine_dataset.csv')

# Create LSTM model
model = create_lstm_model(input_shape=(X_train.shape[1], 1))

# Train model
model.fit(X_train, y_train, epochs=20, batch_size=32, validation_data=(X_test, y_test))

# Save trained model
model.save("../model_weights/pred_oilChange.h5")

print("Trained model saved as pred_oilChange.h5")
