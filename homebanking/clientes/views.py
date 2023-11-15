from django.shortcuts import render
from .models import Cliente


def index(request, user_id):
    try:
        cliente = Cliente.objects.get(pk=user_id)
    except:
        return render(request, "clientes/cliente.html")

    info_cliente = {
        "usuario": cliente.user,
        "tipo_cliente": cliente.tipo_cliente,
        "nombre": cliente.customer_name,
        "apellido": cliente.customer_surname,
        "dni": cliente.customer_dni,
        "fecha_nacimiento": cliente.dob,
        "sucursal": cliente.branch_id,
    }

    context = {"info_cliente": info_cliente}

    return render(request, "clientes/cliente.html", context)
