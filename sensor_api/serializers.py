from rest_framework import serializers
from .models import VehicleSensorData, History

class VehicleSensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSensorData
        fields = '__all__'

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = [
            'id', 'vehicle_id', 'timestamp', 'prediction_result',
            'engine_rpm', 'lub_oil_pressure', 'fuel_pressure',
            'coolant_pressure', 'lub_oil_temp', 'coolant_temp',
            'health_score', 'risk_level', 'lstm_prediction',
            'km_for_coolant_change', 'km_for_oil_change'
        ]
        read_only_fields = ['timestamp']