from django.db import models
from clientes.models import Cliente


class Prestamo(models.Model):
    loan_type = models.CharField(max_length=100)
    loan_date = models.DateTimeField()
    loan_total = models.IntegerField()
    customer_id = models.ForeignKey(Cliente, on_delete=models.CASCADE)

    def __str__(self):
        return f"TIPO_PRESTAMO: {self.loan_type}, ID_CLIENTE: {self.customer_id}, FECHA: {self.loan_date}"

    class Meta:
        db_table = "prestamo"
