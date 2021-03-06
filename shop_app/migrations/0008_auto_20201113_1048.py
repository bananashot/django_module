# Generated by Django 3.1.2 on 2020-11-13 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0007_return_request_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterField(
            model_name='purchase',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='product', to='shop_app.products'),
        ),
    ]
