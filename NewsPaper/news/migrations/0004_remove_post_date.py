# Generated by Django 4.0.4 on 2022-04-22 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_rename_datacreation_post_datecreation_post_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date',
        ),
    ]
