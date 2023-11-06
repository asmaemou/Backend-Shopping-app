# Generated by Django 4.2.6 on 2023-11-05 21:35

from django.db import migrations, models
import pictures.models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0009_alter_shippingdetail_estimated_delivery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_picture',
        ),
        migrations.AddField(
            model_name='product',
            name='picture',
            field=pictures.models.PictureField(aspect_ratios=[None], breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, default='path/to/default/avatar.jpg', file_types=['WEBP'], grid_columns=12, height_field='picture_height', pixel_densities=[1, 2], upload_to='avatars', width_field='picture_width'),
        ),
        migrations.AddField(
            model_name='product',
            name='picture_height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='picture_width',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
