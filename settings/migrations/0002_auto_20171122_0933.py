# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='key',
            field=models.CharField(default=b'', max_length=20),
        ),
        migrations.AlterField(
            model_name='settings',
            name='value',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
