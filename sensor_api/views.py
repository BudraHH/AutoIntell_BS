from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import VehicleSensorData
from .serializers import VehicleSensorDataSerializer

# ViewSet for CRUD

class VehicleSensorDataViewSet(viewsets.ModelViewSet):
    queryset = VehicleSensorData.objects.all().order_by('-timestamp')
    serializer_class = VehicleSensorDataSerializer
    permission_classes = [IsAuthenticated]

# API to get latest sensor data for a specific vehicle

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_latest_sensor_data(request,vehicle_id):
    data = VehicleSensorData.objects.filter(vehicle_id=vehicle_id).order_by('-timestamp')
    if data:
        serializer = VehicleSensorDataSerializer(data)
        return Response(serializer.data)
    return Response({'message' : 'No data found'},status=status.HTTP_404_NOT_FOUND)