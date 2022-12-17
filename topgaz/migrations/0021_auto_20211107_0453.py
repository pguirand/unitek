# Generated by Django 3.1.4 on 2021-11-07 04:53

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topgaz', '0020_transaction_currency'),
    ]

    operations = [
        migrations.RenameField(
            model_name='caisse',
            old_name='total_apports',
            new_name='total_app',
        ),
        migrations.RenameField(
            model_name='caisse',
            old_name='total_depenses',
            new_name='total_appus',
        ),
        migrations.AddField(
            model_name='caisse',
            name='total_buyus',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=7),
        ),
        migrations.AddField(
            model_name='caisse',
            name='total_dep',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=7),
        ),
        migrations.AddField(
            model_name='caisse',
            name='total_depus',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=7),
        ),
        migrations.AddField(
            model_name='caisse',
            name='total_equiht',
            field=models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=7),
        ),
    ]