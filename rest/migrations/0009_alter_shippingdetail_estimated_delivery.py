# Generated by Django 4.2.6 on 2023-11-05 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0008_alter_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingdetail',
            name='estimated_delivery',
            field=models.DateField(),
        ),
    ]
