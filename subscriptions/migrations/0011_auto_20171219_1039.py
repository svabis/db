# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0010_auto_20171219_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timelimittype',
            name='weekday1_end_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='timelimittype',
            name='weekday1_start_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='timelimittype',
            name='weekday2_end_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='timelimittype',
            name='weekday2_start_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='timelimittype',
            name='weekend_end_time',
            field=models.TimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='timelimittype',
            name='weekend_start_time',
            field=models.TimeField(null=True, blank=True),
        ),
    ]
