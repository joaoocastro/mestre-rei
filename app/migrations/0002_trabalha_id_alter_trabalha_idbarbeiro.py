# Generated by Django 4.2.17 on 2024-12-17 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trabalha',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trabalha',
            name='idBarbeiro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.barbeiro', verbose_name='Barbeiro'),
        ),
    ]
