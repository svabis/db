# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0026_abonementtype_extra'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abonementu_apmaksa',
            name='deposit',
        ),
        migrations.RemoveField(
            model_name='abonementu_apmaksa',
            name='gift_card',
        ),
    ]
