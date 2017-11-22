# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_auto_20171122_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='key',
            field=models.CharField(default=b'', max_length=40),
        ),
        migrations.AlterField(
            model_name='settings',
            name='value',
            field=models.CharField(default=b'', max_length=40),
        ),
    ]
