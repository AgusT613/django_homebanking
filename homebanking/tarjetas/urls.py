from django.urls import path
from django.views.generic import ListView
from . import views
from .models import Tarjeta
from .views import ListarTarjetas

urlpatterns = [path("", ListarTarjetas.as_view())]