# Generated by Django 4.2.17 on 2024-12-17 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_trabalha_id_alter_trabalha_idbarbeiro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabalha',
            name='idBarbeiro',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.barbeiro', verbose_name='Barbeiro'),
        ),
    ]