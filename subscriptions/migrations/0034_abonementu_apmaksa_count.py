# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0033_abonementu_apmaksa_deposit'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementu_apmaksa',
            name='count',
            field=models.IntegerField(default=1),
        ),
    ]
