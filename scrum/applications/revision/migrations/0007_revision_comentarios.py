# Generated by Django 3.1.6 on 2021-02-24 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revision', '0006_auto_20210223_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='revision',
            name='comentarios',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Impedimentos'),
        ),
    ]