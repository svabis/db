# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0015_auto_20180225_2124'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementtype',
            name='s3_nr',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]
