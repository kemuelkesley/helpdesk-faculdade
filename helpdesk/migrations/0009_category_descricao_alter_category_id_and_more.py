# Generated by Django 4.2.5 on 2023-09-13 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0008_alter_ticket_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='descricao',
            field=models.CharField(help_text='Criar descrição para a categoria', max_length=50, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Criar categoria para o chamado', max_length=50, null=True, verbose_name='Nome'),
        ),
    ]
