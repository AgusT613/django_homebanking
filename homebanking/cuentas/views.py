from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Cuenta
from clientes.models import Cliente


@login_required(login_url="/login/")
def index(request, user_id):
    cliente = Cliente.objects.get(user_id=user_id)
    cuenta_usuario = Cuenta.objects.filter(customer_id=cliente)
    datos = [cuenta for cuenta in cuenta_usuario]

    context = {"cuenta": datos, "cliente": cliente, "id_cliente": user_id}

    return render(request, "cuentas/informacion.html", context)

def crear_cuenta(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo')
        saldo = request.POST.get('saldo')
        iban = request.POST.get('iban')

        if tipo and saldo and iban:
            nueva_cuenta = Cuenta(tipo=tipo, saldo=saldo, iban=iban, cliente=request.user.cliente)
            nueva_cuenta.save()

    return render(request, "cuentas/crear_cuenta.html")