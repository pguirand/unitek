# Generated by Django 3.1.4 on 2022-02-03 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topgaz', '0058_creance'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creance',
            old_name='montant',
            new_name='dette',
        ),
        migrations.RenameField(
            model_name='creance',
            old_name='solde',
            new_name='paiement',
        ),
        migrations.RemoveField(
            model_name='creance',
            name='type',
        ),
    ]