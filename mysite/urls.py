from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('polls/', include("polls.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación proporcionadas por Django
    path('sign_up/', include('authentication.urls')),  # Incluye las URLs de la aplicación de autenticación
]
