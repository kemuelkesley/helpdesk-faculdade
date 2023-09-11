# Generated by Django 4.2.5 on 2023-09-09 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_alter_condominio_nome'),
        ('helpdesk', '0002_remove_ticket_condominio'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='condominio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cadastro.condominio', verbose_name='Condomínio'),
            preserve_default=False,
        ),
    ]