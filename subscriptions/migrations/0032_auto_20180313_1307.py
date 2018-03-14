# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0031_abonementu_iesalde'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementu_iesalde',
            name='freeze_from',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='abonementu_iesalde',
            name='freeze_until',
            field=models.DateField(null=True, blank=True),
        ),
    ]
