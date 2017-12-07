# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0005_auto_20171208_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonementi',
            name='best_before',
            field=models.IntegerField(default=0, null=True, blank=True),
        ),
    ]
