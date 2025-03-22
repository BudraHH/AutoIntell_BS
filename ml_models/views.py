from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from ml_models.engine_health_model.predict import predict_engine_health


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_engine_health_prediction(request):
    data = request.data
    predictions = predict_engine_health(
        data['Engine rpm'],
        data['Lub oil pressure'],
        data['Fuel pressure'],
        data['Coolant pressure'],
        data['Lub oil temp'],
        data['Coolant temp']
    )
    return Response(predictions)