from django.db import models
from cuentas.models import Cuenta


class Movimientos(models.Model):
    account = models.ForeignKey(Cuenta, models.DO_NOTHING, blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    operation_type = models.CharField(blank=True, null=True, max_length=200)
    movement_time = models.DateTimeField()

    def __str__(self):
        return (
            f"CUENTA: {self.account}, MONTO: {self.amount}, FECHA: {self.movement_time}"
        )

    class Meta:
        db_table = "movimientos"
