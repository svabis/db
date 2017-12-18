# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import subscriptions.models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0004_abonementtype_position'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelimitType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=60)),
                ('weekday', models.IntegerField(null=True, blank=True)),
                ('start_time', models.TimeField(default=subscriptions.models.default_start_time)),
                ('end_time', models.TimeField(default=subscriptions.models.default_start_time)),
            ],
            options={
                'db_table': 'laika_limiti_tipi',
            },
        ),
    ]
