from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleSensorDataViewSet, get_latest_sensor_data

router = DefaultRouter()
router.register(r'data', VehicleSensorDataViewSet, basename='vehicle-sensor')

urlpatterns = [
    path('', include(router.urls)),
    path('latest/<str:vehicle_id>/', get_latest_sensor_data, name='latest-sensor-data'),
]
