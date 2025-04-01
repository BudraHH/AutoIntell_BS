from django.db import models
from django.utils.timezone import now

class VehicleSensorData(models.Model):
    vehicle_id = models.AutoField(primary_key=True)
    engine_temperature = models.FloatField()
    battery_voltage = models.FloatField()
    brake_pressure = models.FloatField()
    tire_pressure = models.FloatField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return f'VehicleSensorData: {self.timestamp}'

class History(models.Model):
    vehicle_id = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    prediction_result = models.CharField(max_length=1)
    engine_rpm = models.FloatField()
    lub_oil_pressure = models.FloatField()
    fuel_pressure = models.FloatField()
    coolant_pressure = models.FloatField()
    lub_oil_temp = models.FloatField()
    coolant_temp = models.FloatField()
    health_score = models.FloatField()
    risk_level = models.CharField(max_length=20)
    lstm_prediction = models.FloatField()
    km_for_coolant_change = models.FloatField()
    km_for_oil_change = models.FloatField()

    def __str__(self):
        return f"{self.vehicle_id} - {self.timestamp}"
