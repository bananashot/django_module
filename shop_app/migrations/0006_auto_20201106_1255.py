# Generated by Django 3.1.2 on 2020-11-06 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_auto_20201030_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='number',
            field=models.PositiveIntegerField(),
        ),
    ]
