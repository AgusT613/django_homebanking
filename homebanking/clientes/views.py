from django.shortcuts import render
from .models import Cliente
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def index(request, user_id):
    try:
        cliente = Cliente.objects.get(user_id=user_id)
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

    context = {"info_cliente": info_cliente, "id_cliente": user_id}

    return render(request, "clientes/cliente.html", context)
