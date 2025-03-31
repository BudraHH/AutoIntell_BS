from rest_framework import serializers
from .models import VehicleSensorData

class VehicleSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSensorData
        fields = '__all__'