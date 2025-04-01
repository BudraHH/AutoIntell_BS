import tensorflow as tf
from keras import Sequential , layers
# from keras.layers import LSTM, Dense


def create_lstm_model(input_shape):
    model = Sequential([
        layers.LSTM(50, return_sequences=True, input_shape=input_shape),
        layers.LSTM(50, return_sequences=False),
        layers.Dense(25, activation='relu'),
        layers.Dense(1)  # Output layer for regression
    ])

    # Compile model
    model.compile(optimizer='adam', loss='mse')
    return model
