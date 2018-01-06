# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import subscriptions.models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0009_auto_20171219_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelimittype',
            name='weekday2',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='timelimittype',
            name='weekday2_end_time',
            field=models.TimeField(default=subscriptions.models.default_start_time),
        ),
        migrations.AddField(
            model_name='timelimittype',
            name='weekday2_start_time',
            field=models.TimeField(default=subscriptions.models.default_start_time),
        ),
    ]
