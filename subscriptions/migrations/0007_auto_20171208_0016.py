# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0006_auto_20171208_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonementi',
            name='best_before',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
