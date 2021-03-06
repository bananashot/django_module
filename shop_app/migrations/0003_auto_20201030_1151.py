# Generated by Django 3.1.2 on 2020-10-30 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0002_auto_20201030_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='return',
            name='declined_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.purchase'),
        ),
    ]
