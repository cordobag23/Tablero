# Generated by Django 3.1.6 on 2021-03-05 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('equipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tareas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, verbose_name='Descripción de la tarea')),
                ('estado', models.CharField(max_length=50, verbose_name='Estado de la tarea')),
                ('equipo_tarea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='equipo.equipo')),
            ],
        ),
    ]
