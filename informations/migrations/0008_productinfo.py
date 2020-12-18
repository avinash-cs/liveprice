# Generated by Django 3.1.4 on 2020-12-17 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('informations', '0007_auto_20201026_1659'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('product_url', models.CharField(max_length=1000)),
                ('product_img', models.CharField(max_length=1000)),
                ('product_price', models.CharField(max_length=100)),
                ('product_seller', models.CharField(max_length=100)),
            ],
        ),
    ]