# Generated by Django 2.2.7 on 2019-12-16 12:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Public_Data_Acquisition_Unit', '0005_auto_20191216_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facebook_target_group',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 12, 23, 30, 111046, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='facebook_target_hashtag',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 12, 23, 30, 111465, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='facebook_target_page',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 12, 23, 30, 110532, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='facebook_target_person',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 12, 23, 30, 110060, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='facebook_target_search',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 12, 23, 30, 111883, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news_site_target',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 12, 23, 30, 113234, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news_site_target',
            name='expired_on',
            field=models.IntegerField(default=7),
        ),
        migrations.AlterField(
            model_name='twitter_target_hashtag',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 12, 23, 30, 112787, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='twitter_target_person',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 16, 12, 23, 30, 112357, tzinfo=utc)),
        ),
    ]