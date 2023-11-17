from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from .models import Tarjeta
from .models import MarcaTarjetas

class ListarTarjetas(ListView):
    model = Tarjeta
    template_name = 'tarjetas.html'
    context_object_name = 'tarjetas'

    def get(self, request, user_id):
        tarjetas = self.get_queryset().filter(cliente=request.user.cliente)
        response = "Tarjetas del Cliente:<br>"
        for tarjeta in tarjetas:
            response += f"Tipo: {tarjeta.tipo}, Número: {tarjeta.numero}<br>"
        return HttpResponse(response)