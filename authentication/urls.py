from django.urls import path, include
from .views import login_user, register_user

urlpatterns = [
    path('sign-in/', login_user, name='sign-in'),
    path('sign-up/', register_user, name='sign-up'),
]