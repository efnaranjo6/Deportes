# Generated by Django 3.0.4 on 2020-04-18 03:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Estadio', '0002_auto_20200417_2242'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estadio',
            old_name='ano_constrccion',
            new_name='ano_construccion',
        ),
    ]
