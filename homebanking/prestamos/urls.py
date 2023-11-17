from django.urls import path
from . import views

urlpatterns = [path("solicitud_prestamo/", views.solicitud_prestamo),]