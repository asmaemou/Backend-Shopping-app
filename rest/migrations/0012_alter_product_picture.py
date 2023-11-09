# Generated by Django 4.2.6 on 2023-11-05 21:45

from django.db import migrations
import pictures.models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0011_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=pictures.models.PictureField(aspect_ratios=[None], blank=True, breakpoints={'l': 1200, 'm': 992, 's': 768, 'xl': 1400, 'xs': 576}, container_width=1200, file_types=['WEBP'], grid_columns=12, height_field='picture_height', null=True, pixel_densities=[1, 2], upload_to='rest/avatars', width_field='picture_width'),
        ),
    ]