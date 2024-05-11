# Generated by Django 5.0.4 on 2024-05-11 14:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abogado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_abogado', models.CharField(max_length=45)),
                ('cedula_abogado', models.DecimalField(decimal_places=0, max_digits=10)),
                ('email', models.EmailField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=45)),
                ('cedula_cliente', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('email', models.EmailField(max_length=45)),
                ('direccion', models.CharField(max_length=45)),
                ('telefono', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Especializacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='TipoContabilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Asesoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_abogado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.abogado')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.cliente')),
            ],
        ),
        migrations.AddField(
            model_name='abogado',
            name='especializacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.especializacion'),
        ),
        migrations.CreateModel(
            name='Proceso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_online', models.CharField(max_length=45)),
                ('doc_fisico', models.CharField(max_length=45)),
                ('id_abogado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.abogado')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.cliente')),
                ('tipo_proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.tipoproceso')),
            ],
        ),
        migrations.CreateModel(
            name='Audiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lugar', models.CharField(max_length=45)),
                ('fecha_hora', models.DateTimeField()),
                ('id_proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.proceso')),
            ],
        ),
        migrations.CreateModel(
            name='ContabilidadProcesos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_proceso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.proceso')),
                ('tipo_contabilidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.tipocontabilidad')),
            ],
        ),
        migrations.CreateModel(
            name='ContabilidadOficina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('id_abogado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.abogado')),
                ('tipo_contabilidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.tipocontabilidad')),
            ],
        ),
    ]
