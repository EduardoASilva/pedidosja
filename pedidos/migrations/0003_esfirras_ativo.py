# Generated by Django 4.2.4 on 2023-09-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_rename_nome_quantidade_id_esfirra'),
    ]

    operations = [
        migrations.AddField(
            model_name='esfirras',
            name='ativo',
            field=models.BooleanField(default=False),
        ),
    ]
