from django.urls import path
from MiApp.views import datos_familiares

urlpatterns = [
    path('familiares/', datos_familiares)
]