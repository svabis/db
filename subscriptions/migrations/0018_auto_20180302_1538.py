# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0017_abonementtype_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abonementi',
            name='frozen',
        ),
        migrations.RemoveField(
            model_name='abonementi',
            name='frozen_until_date',
        ),
    ]
