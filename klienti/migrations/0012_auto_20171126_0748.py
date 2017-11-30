# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0011_auto_20171126_0744'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='phone',
            field=models.CharField(max_length=16, null=True, blank=True),
        ),
    ]
