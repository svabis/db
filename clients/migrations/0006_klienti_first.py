# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0005_auto_20180223_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='klienti',
            name='first',
            field=models.BooleanField(default=False),
        ),
    ]
