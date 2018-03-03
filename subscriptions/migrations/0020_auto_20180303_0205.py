# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0019_auto_20180303_0125'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementtype',
            name='position1',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='abonementtype',
            name='position2',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
