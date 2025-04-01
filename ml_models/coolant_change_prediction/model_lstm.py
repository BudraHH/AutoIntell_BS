import tensorflow as tf
from keras import Sequential , layers
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense, Dropout

def create_lstm_model(input_shape):
    model = Sequential([
        layers.LSTM(50, return_sequences=True, input_shape=input_shape),
        layers.Dropout(0.2),
        layers.LSTM(50),
        layers.Dropout(0.2),
        layers.Dense(25, activation='relu'),
        layers.Dense(1)  # Output layer
    ])

    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model
