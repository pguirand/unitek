# Generated by Django 3.1.4 on 2022-01-29 05:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('topgaz', '0055_auto_20220118_0541'),
    ]

    operations = [
        migrations.AddField(
            model_name='vente',
            name='client',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='achat', to='topgaz.client'),
        ),
    ]
