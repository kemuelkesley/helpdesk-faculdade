# Generated by Django 4.2.5 on 2023-11-05 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0020_alter_categoriaequipamento_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaequipamento',
            options={'ordering': ['-criado_em'], 'verbose_name': 'Categoria de equipamentos', 'verbose_name_plural': 'Categoria'},
        ),
        migrations.AddField(
            model_name='categoriaequipamento',
            name='equipamento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='categoria_equipamento', to='cadastro.equipamento', verbose_name='Equipamento'),
        ),
    ]
