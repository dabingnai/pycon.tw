# Generated by Django 3.0.7 on 2021-02-01 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0020_merge_20210131_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openrole',
            name='description_en_us',
        ),
        migrations.RemoveField(
            model_name='openrole',
            name='description_zh_hant',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='intro_en_us',
        ),
        migrations.RemoveField(
            model_name='sponsor',
            name='intro_zh_hant',
        ),
    ]
