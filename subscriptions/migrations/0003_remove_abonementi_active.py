# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_auto_20171207_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abonementi',
            name='active',
        ),
    ]
