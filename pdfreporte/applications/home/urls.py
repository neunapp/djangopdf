from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    path(
        'listar-empleados/',
        views.ListEmpleadosPdf.as_view(),
        name='empleados_all'
    ),
]