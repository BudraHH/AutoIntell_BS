from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleSensorDataViewSet, get_latest_sensor_data, HistoryViewSet

router = DefaultRouter()
router.register(r'data', VehicleSensorDataViewSet, basename='vehicle-sensor')

urlpatterns = [
    path('', include(router.urls)),
    path('latest/<str:vehicle_id>/', get_latest_sensor_data, name='latest-sensor-data'),
    path('history/', HistoryViewSet.as_view({'post': 'create'}), name='save-history'),
    path('history/<str:vehicle_id>/', HistoryViewSet.as_view({'get': 'list'}), name='get-history'),
]
