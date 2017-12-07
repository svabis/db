# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_remove_abonementi_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementi',
            name='special',
            field=models.BooleanField(default=False),
        ),
    ]
