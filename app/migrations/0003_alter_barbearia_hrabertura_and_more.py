# Generated by Django 5.0.4 on 2024-04-21 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_barbearia_cliente_agendamento_trabalha'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barbearia',
            name='hrAbertura',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='barbearia',
            name='hrFechamento',
            field=models.TimeField(null=True),
        ),
    ]
