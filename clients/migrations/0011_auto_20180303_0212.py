# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_auto_20180302_0923'),
    ]

    operations = [
        migrations.AddField(
            model_name='klienti',
            name='frozen',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='klienti',
            name='frozen_from',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='klienti',
            name='frozen_until',
            field=models.DateField(null=True, blank=True),
        ),
    ]
