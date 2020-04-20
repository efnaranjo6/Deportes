# Generated by Django 3.0.4 on 2020-04-19 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Ciudad', '0001_initial'),
        ('Empresa', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empresa',
            name='Ciudad',
        ),
        migrations.AddField(
            model_name='empresa',
            name='ciudad',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='Ciudad.Ciudad'),
            preserve_default=False,
        ),
    ]