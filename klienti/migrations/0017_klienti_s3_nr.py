# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0016_auto_20171201_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='klienti',
            name='s3_nr',
            field=models.CharField(default=b'', max_length=10),
        ),
    ]
