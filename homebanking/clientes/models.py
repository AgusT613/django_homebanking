from django.db import models
from django.contrib.auth.models import User


class TipoCliente(models.Model):
    tipo = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = "tipo_cliente"


class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_cliente = models.ForeignKey(TipoCliente, on_delete=models.DO_NOTHING)
    customer_name = models.CharField(max_length=100)
    customer_surname = models.CharField(max_length=100)
    customer_dni = models.CharField(
        db_column="customer_DNI", max_length=8
    )  # Field name made lowercase.
    dob = models.DateField()
    branch_id = (
        models.IntegerField()
    )  # Could not use a foreign key due to an import problem

    def __str__(self):
        return f"USUARIO: {self.user}, TIPO_CLIENTE: {self.tipo_cliente}, NOMBRE_COMPLETO: {self.customer_name} {self.customer_surname}, DNI: {self.customer_dni}"

    class Meta:
        db_table = "cliente"
