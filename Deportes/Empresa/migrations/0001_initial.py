# Generated by Django 3.0.4 on 2020-04-19 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Ciudad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('representante', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('Ciudad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ciudad.Ciudad')),
            ],
        ),
    ]