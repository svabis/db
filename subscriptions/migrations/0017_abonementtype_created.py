# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0016_abonementtype_s3_nr'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementtype',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
