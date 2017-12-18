# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import subscriptions.models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0006_abonementtype_time_limit_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timelimittype',
            old_name='end_time',
            new_name='weekday_end_time',
        ),
        migrations.RenameField(
            model_name='timelimittype',
            old_name='start_time',
            new_name='weekday_start_time',
        ),
        migrations.AddField(
            model_name='timelimittype',
            name='weekend',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='timelimittype',
            name='weekend_end_time',
            field=models.TimeField(default=subscriptions.models.default_start_time),
        ),
        migrations.AddField(
            model_name='timelimittype',
            name='weekend_start_time',
            field=models.TimeField(default=subscriptions.models.default_start_time),
        ),
        migrations.AlterField(
            model_name='timelimittype',
            name='weekday',
            field=models.BooleanField(default=False),
        ),
    ]
