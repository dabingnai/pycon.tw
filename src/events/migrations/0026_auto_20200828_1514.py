# Generated by Django 3.0.3 on 2020-08-28 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0025_joblistingsevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keynoteevent',
            name='slug',
            field=models.SlugField(help_text="This is used to link to the speaker's introduction on the Keynote page, e.g. 'liang2' will link to '/en-us/conference/keynotes/#keynote-speaker-liang2'.", verbose_name='slug'),
        ),
    ]
