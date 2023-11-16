from django.urls import path
from . import views

urlpatterns = [path("<int:user_id>/", views.index),
               path("crearcuenta/", views.crear_cuenta)]
