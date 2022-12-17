# Generated by Django 3.1.4 on 2021-10-29 16:02

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topgaz', '0007_auto_20211029_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='caisse',
            name='ap_meter',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0.00'), max_digits=7),
        ),
        migrations.AlterField(
            model_name='caisse',
            name='av_meter',
            field=models.DecimalField(blank=True, decimal_places=1, default=Decimal('0.00'), max_digits=7),
        ),
        migrations.CreateModel(
            name='Vente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inmeter', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0.00'), max_digits=7)),
                ('outmeter', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0.00'), max_digits=7)),
                ('pgal', models.IntegerField(blank=True, default=0)),
                ('nbgal', models.DecimalField(blank=True, decimal_places=1, default=Decimal('0.00'), max_digits=7)),
                ('bycash', models.IntegerField(blank=True, default=0)),
                ('caisse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topgaz.caisse')),
            ],
        ),
    ]