# Generated by Django 4.2.4 on 2023-09-21 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quantidade',
            old_name='nome',
            new_name='id_esfirra',
        ),
    ]
