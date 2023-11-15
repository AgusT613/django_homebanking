from django.contrib import admin
from .models import Tarjeta, MarcaTarjetas

admin.site.register([Tarjeta, MarcaTarjetas])
