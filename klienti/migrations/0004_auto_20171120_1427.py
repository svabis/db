# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0003_auto_20171120_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='notes',
            field=models.CharField(default=b'', max_length=150, blank=True),
        ),
    ]
