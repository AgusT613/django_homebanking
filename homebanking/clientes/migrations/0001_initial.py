# Generated by Django 4.2.7 on 2023-11-14 23:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'db_table': 'tipo_cliente',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_surname', models.CharField(max_length=100)),
                ('customer_dni', models.CharField(db_column='customer_DNI', max_length=8)),
                ('dob', models.DateField()),
                ('branch_id', models.IntegerField()),
                ('tipo_cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='clientes.tipocliente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]
