# Generated by Django 4.2.5 on 2023-09-09 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0005_rename_nnumero_identificacao_condominio_numero_identificacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='condominio',
            name='nome',
            field=models.CharField(help_text='Infome o nome do Condominio', max_length=50, verbose_name='Nome do Condominio'),
        ),
    ]
