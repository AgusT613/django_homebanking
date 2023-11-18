from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tarjeta
from clientes.models import Cliente


@login_required(login_url="/")
def listarTarjetas(request, user_id):
    ruta_template = "tarjetas/tarjetas.html"
    try:
        cliente = Cliente.objects.get(user_id=user_id)
    except:
        context = {"sin_clientes": True}
        return render(request, ruta_template, context)

    try:
        tarjetas = Tarjeta.objects.filter(customer_id=cliente)
    except:
        return render(request, ruta_template)

    context = {
        "tarjetas": tarjetas,
        "id_cliente": user_id,
        "nombre_cliente": cliente.customer_name,
    }
    return render(request, ruta_template, context)
