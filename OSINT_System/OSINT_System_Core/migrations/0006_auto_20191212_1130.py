# Generated by Django 2.2.7 on 2019-12-12 11:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('OSINT_System_Core', '0005_auto_20191210_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supported_socail_sites',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2019, 12, 12, 11, 30, 46, 580604, tzinfo=utc)),
        ),
    ]