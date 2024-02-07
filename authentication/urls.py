# authentication/urls.py

from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('register/', views.sign_up, name='sign_up'),
    # otras URL de autenticación si las tienes
]
