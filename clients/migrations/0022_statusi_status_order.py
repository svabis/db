# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0021_auto_20180403_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusi',
            name='status_order',
            field=models.IntegerField(default=0),
        ),
    ]
