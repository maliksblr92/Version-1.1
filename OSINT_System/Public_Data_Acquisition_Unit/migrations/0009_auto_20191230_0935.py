# Generated by Django 2.2.7 on 2019-12-30 09:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Public_Data_Acquisition_Unit', '0008_auto_20191230_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='twitter_target_person',
            name='tweets_type',
            field=models.CharField(default='from', max_length=20),
        ),
        migrations.AlterField(
            model_name='facebook_target_group',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 489552, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='facebook_target_hashtag',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 490018, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='facebook_target_page',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 489092, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='facebook_target_person',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 488504, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='facebook_target_search',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 490436, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='instagram_target_person',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 492839, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='instagram_target_search',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 493385, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='news_site_target',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 492276, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='twitter_target_hashtag',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 491392, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='twitter_target_person',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 490945, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='twitter_target_search',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 30, 9, 35, 7, 491843, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='twitter_target_search',
            name='search_type',
            field=models.CharField(choices=[('phrase', 'search using text phrase'), ('hashtag', 'search using hastags'), ('location', 'search using location'), ('bydate', 'search using date')], max_length=50),
        ),
    ]
