# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonementi',
            name='best_before',
            field=models.CharField(max_length=3, null=True, blank=True),
        ),
    ]
