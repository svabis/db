# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0009_auto_20180406_2319'),
    ]

    operations = [
        migrations.AddField(
            model_name='reports',
            name='event_data',
            field=models.CharField(default=b'', max_length=200),
        ),
        migrations.AlterField(
            model_name='reports',
            name='event',
            field=models.CharField(max_length=100),
        ),
    ]
