# Generated by Django 3.1.4 on 2021-12-06 02:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('topgaz', '0031_auto_20211206_0216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='username',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contact', to=settings.AUTH_USER_MODEL),
        ),
    ]
