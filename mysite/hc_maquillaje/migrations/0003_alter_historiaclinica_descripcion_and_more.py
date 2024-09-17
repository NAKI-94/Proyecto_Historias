# Generated by Django 5.1.1 on 2024-09-17 02:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hc_maquillaje', '0002_historiaclinica_descripcion_historiaclinica_fecha'),
        ('pacientes', '0002_historiaclinica'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historiaclinica',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='fecha',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='historiaclinica',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='historias_clinicas_hc_maquillaje', to='pacientes.paciente'),
        ),
    ]
