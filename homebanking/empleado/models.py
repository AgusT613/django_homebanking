from django.db import models


class Empleado(models.Model):
    employee_name = models.CharField(max_length=100)
    employee_surname = models.CharField(max_length=100)
    employee_hire_date = models.DateTimeField()
    employee_dni = models.CharField(
        db_column="employee_DNI", max_length=8
    )  # Field name made lowercase.
    branch_id = models.IntegerField(
        null=True
    )  # Could not use the foreign key due to an import problem

    class Meta:
        db_table = "empleado"
