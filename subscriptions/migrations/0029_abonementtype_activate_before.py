# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0028_auto_20180307_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementtype',
            name='activate_before',
            field=models.IntegerField(default=1, null=True, blank=True),
        ),
    ]
