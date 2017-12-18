# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_timelimittype'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementtype',
            name='time_limit_type',
            field=models.ForeignKey(blank=True, to='subscriptions.TimelimitType', null=True),
        ),
    ]
