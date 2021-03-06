# Generated by Django 3.0.4 on 2020-04-20 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Jugador', '0001_initial'),
        ('Equipo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='JugadorTemporada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechainicial', models.DateField()),
                ('fechafinal', models.DateField()),
                ('Equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Equipo.Equipo')),
                ('Jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Jugador.Jugador')),
            ],
        ),
    ]
