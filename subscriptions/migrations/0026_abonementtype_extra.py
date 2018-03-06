# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0025_abonementu_apmaksa'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementtype',
            name='extra',
            field=models.BooleanField(default=False),
        ),
    ]
