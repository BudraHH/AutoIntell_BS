from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ml_models.engine_health_model.predict import predict_engine_health
from ml_models.coolant_change_prediction.predict import predict_coolant_change  # Import the coolant change prediction function
from ml_models.oil_change_prediction.predict import predict_oil_change  # Import the oil change prediction function

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_engine_health_prediction(request):
    data = request.data

    # Get prediction from engine health model
    engine_health_prediction = predict_engine_health(
        data['Engine rpm'],
        data['Lub oil pressure'],
        data['Fuel pressure'],
        data['Coolant pressure'],
        data['Lub oil temp'],
        data['Coolant temp']
    )

    # Calculate risk level based on lstm prediction
    health_score = round(engine_health_prediction['lstm_prediction'], 2)
    risk_level = "High" if health_score < 0.4 else "Medium" if health_score < 0.7 else "Low"

    # Pass the required values to the coolant change prediction function
    km_for_coolant_change = predict_coolant_change(
        data['Coolant temp'],
        data['Coolant pressure'],
        data['Engine rpm'],
        data['Lub oil temp'],
        data['Lub oil pressure'],
        data['Fuel pressure']
    )

    # Pass the required values to the oil change prediction function
    km_for_oil_change = predict_oil_change(
        data['Lub oil pressure'],
        data['Engine rpm'],
        data['Coolant pressure'],
        data['Lub oil temp'],
        data['Coolant temp']
    )

    # Response JSON
    response_data = {
        "prediction": engine_health_prediction,  # LSTM prediction results
        "health_score": health_score,
        "risk_level": risk_level,
        "km_for_coolant_change": km_for_coolant_change,  # Km left for coolant change prediction
        "km_for_oil_change": km_for_oil_change,  # Km left for oil change prediction
    }

    return Response(response_data)
