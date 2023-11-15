from django.db import models
from clientes.models import Cliente


class MarcaTarjetas(models.Model):
    marca = models.CharField(max_length=200)

    def __str__(self):
        return self.marca

    class Meta:
        db_table = "marca_tarjetas"


class Tarjeta(models.Model):
    numero = models.CharField(max_length=250)
    cvv = models.CharField(max_length=4)
    fecha_otorgamiento = models.DateField()
    fecha_expiracion = models.DateField()
    tipo = models.CharField(max_length=100)
    marca_tarjeta_id = models.ForeignKey(
        MarcaTarjetas,
        models.DO_NOTHING,
        db_column="marcaTarjetaId",
    )  # Field name made lowercase.
    customer_id = models.ForeignKey(Cliente, models.DO_NOTHING, db_column="customerId")
    # Field name made lowercase.

    def __str__(self):
        return f"EXPIRACION: {self.fecha_expiracion}, MARCA_TARJETA_ID: {self.marca_tarjeta_id}, CLIENTE_ID: {self.customer_id}"

    class Meta:
        db_table = "tarjeta"
