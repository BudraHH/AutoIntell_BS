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
