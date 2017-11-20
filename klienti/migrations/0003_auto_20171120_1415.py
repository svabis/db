# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0002_auto_20171116_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='klienti',
            name='card_blocked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='klienti',
            name='client_blocked',
            field=models.BooleanField(default=False),
        ),
    ]
