import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv('../datasets/engine_dataset.csv')

# Estimating a proxy for kilometers left before an oil change based on heuristics
df['Km Left Before Oil Change'] = (df['Lub oil pressure'] * 10) + (df['lub oil temp'] * -1) + \
                                  (df['Engine rpm'] * 0.05) + (df['Coolant pressure'] * 3) + \
                                  (df['Coolant temp'] * 0.3)

# Feature and target
X = df[['Lub oil pressure', 'Engine rpm', 'Coolant pressure', 'lub oil temp', 'Coolant temp']]
y = df['Km Left Before Oil Change']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model creation (Random Forest Regressor)
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Predicting for a new data point
new_data = [[3.5, 1000, 2, 80, 85]]  # Example data (Lub oil pressure in bar)
predicted_km_left = model.predict(new_data)
print(f'Predicted Km Left Before Oil Change: {predicted_km_left[0]} km')
