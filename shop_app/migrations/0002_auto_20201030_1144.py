# Generated by Django 3.1.2 on 2020-10-30 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='product_name',
            field=models.CharField(max_length=120),
        ),
    ]