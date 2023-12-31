# Generated by Django 4.2.7 on 2023-11-14 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoCuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'db_table': 'tipo_cuenta',
            },
        ),
        migrations.CreateModel(
            name='Cuenta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('iban', models.CharField(max_length=200)),
                ('tipocuenta', models.ForeignKey(blank=True, db_column='tipoCuenta', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='cuentas.tipocuenta')),
            ],
            options={
                'db_table': 'cuenta',
            },
        ),
    ]
