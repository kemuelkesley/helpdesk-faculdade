# Generated by Django 4.2.5 on 2023-11-05 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0014_alter_comentario_comentario_alter_comentario_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='comentario_fechamento',
            field=models.TextField(blank=True, null=True, verbose_name='Comentário de Fechamento'),
        ),
    ]
