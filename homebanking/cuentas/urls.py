from django.urls import path
from . import views

urlpatterns = [
    path("<int:user_id>/", views.index, name="cuentas"),
    path("crear/<int:user_id>", views.crear_cuenta, name="crear_cuenta"),
]
