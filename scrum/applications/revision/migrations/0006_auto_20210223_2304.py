# Generated by Django 3.1.6 on 2021-02-24 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('impedimentos', '0001_initial'),
        ('revision', '0005_auto_20210223_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='revision',
            name='impedimentos',
        ),
        migrations.AddField(
            model_name='revision',
            name='impedimentos',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='impedimentos.impedimentos'),
        ),
    ]