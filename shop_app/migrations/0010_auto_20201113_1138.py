# Generated by Django 3.1.2 on 2020-11-13 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0009_auto_20201113_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return',
            name='request_status',
            field=models.CharField(blank=True, default='Action required', max_length=120, null=True),
        ),
    ]
