# Generated by Django 3.1.2 on 2020-11-15 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0013_auto_20201113_1220'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='products',
            new_name='product',
        ),
    ]
