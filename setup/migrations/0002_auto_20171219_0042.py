# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='value',
            field=models.CharField(max_length=40, blank=True),
        ),
    ]
