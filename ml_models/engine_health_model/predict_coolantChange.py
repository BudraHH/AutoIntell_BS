import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Load dataset
df = pd.read_csv('../datasets/engine_dataset.csv')

# Feature Engineering - Approximate heuristic for coolant change prediction
df['Km Left Before Coolant Change'] = (df['Coolant temp'] * -0.5) + (df['Coolant pressure'] * 10) + \
                                      (df['Engine rpm'] * 0.03) + (df['lub oil temp'] * -0.2) + \
                                      (df['Lub oil pressure'] * 5) + (df['Fuel pressure'] * 2)

# Defining features and target variable
X = df[['Coolant temp', 'Coolant pressure', 'Engine rpm', 'lub oil temp', 'Lub oil pressure', 'Fuel pressure']]
y = df['Km Left Before Coolant Change']

# Splitting dataset into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Random Forest model
model = RandomForestRegressor(n_estimators=150, random_state=42)
model.fit(X_train, y_train)

# Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')

# Predicting for a new input sample
new_data = [[85, 1.8, 2500, 90, 4, 2.5]]  # Example values: coolant temp, pressure, RPM, oil temp, oil pressure, fuel pressure
predicted_km_left = model.predict(new_data)

print(f'Predicted Km Left Before Coolant Change: {predicted_km_left[0]:.2f} km')
