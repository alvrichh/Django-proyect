# authentication/urls.py

from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('sign_up/', views.sign_up, name='sign_up'),
    # otras URL de autenticación si las tienes
]
