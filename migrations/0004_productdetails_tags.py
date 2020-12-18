# Generated by Django 3.1.2 on 2020-10-20 05:28

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('informations', '0003_auto_20201020_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
