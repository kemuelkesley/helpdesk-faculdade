# Generated by Django 4.2.5 on 2023-09-09 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Condominiomodel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero_identificacao', models.PositiveIntegerField(default=1, help_text='Número de identificação do condomínio', unique=True, verbose_name='Número de Identificação')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome do Condomínio')),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
