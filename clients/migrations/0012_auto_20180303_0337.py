# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_auto_20180303_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='phone',
            field=models.CharField(max_length=30, null=True, blank=True),
        ),
    ]
