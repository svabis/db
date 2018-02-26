# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0014_abonementi'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementi',
            name='frozen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='abonementi',
            name='frozen_until_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
