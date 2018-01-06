# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0008_auto_20171218_2319'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timelimittype',
            old_name='weekday',
            new_name='weekday1',
        ),
        migrations.RenameField(
            model_name='timelimittype',
            old_name='weekday_end_time',
            new_name='weekday1_end_time',
        ),
        migrations.RenameField(
            model_name='timelimittype',
            old_name='weekday_start_time',
            new_name='weekday1_start_time',
        ),
    ]
