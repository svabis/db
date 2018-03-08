# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0029_abonementtype_activate_before'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abonementu_apmaksa',
            name='card',
        ),
        migrations.RemoveField(
            model_name='abonementu_apmaksa',
            name='cash',
        ),
    ]
