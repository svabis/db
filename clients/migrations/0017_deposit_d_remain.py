# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0016_auto_20180307_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='d_remain',
            field=models.DecimalField(default=0, max_digits=5, decimal_places=2),
        ),
    ]
