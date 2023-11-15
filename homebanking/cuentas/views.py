from django.shortcuts import render
from .models import Cuenta
from clientes.models import Cliente


def index(request, user_id):
    cliente = Cliente.objects.get(pk=user_id)
    cuenta_usuario = Cuenta.objects.filter(customer_id=cliente)
    datos = [cuenta for cuenta in cuenta_usuario]

    context = {"cuenta": datos, "cliente": cliente}

    return render(request, "cuentas/informacion.html", context)
