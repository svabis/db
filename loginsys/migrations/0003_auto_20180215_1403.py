# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0002_auto_20180215_1359'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='log',
            table='log',
        ),
    ]
