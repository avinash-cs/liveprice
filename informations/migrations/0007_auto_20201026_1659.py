# Generated by Django 3.1.2 on 2020-10-26 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0006_auto_20201026_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='product_image',
            field=models.URLField(max_length=3000),
        ),
    ]