# Generated by Django 3.0.4 on 2020-04-18 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Estadio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estadio',
            name='ano_constrccion',
            field=models.DateField(),
        ),
    ]