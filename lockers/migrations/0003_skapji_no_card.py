# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lockers', '0002_skapji_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='skapji',
            name='no_card',
            field=models.BooleanField(default=False),
        ),
    ]
