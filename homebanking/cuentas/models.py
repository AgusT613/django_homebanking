from django.db import models


class TipoCuenta(models.Model):
    descripcion = models.CharField(unique=True, max_length=200)

    def __str__(self):
        return f"DESCRIPCION: {self.descripcion}"

    class Meta:
        db_table = "tipo_cuenta"


class Cuenta(models.Model):
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.CharField(max_length=200)
    tipocuenta = models.ForeignKey(
        TipoCuenta, models.DO_NOTHING, db_column="tipoCuenta", blank=True, null=True
    )  # Field name made lowercase.

    def __str__(self):
        return f"TIPO_CUENTA: {self.tipocuenta}"

    class Meta:
        db_table = "cuenta"
