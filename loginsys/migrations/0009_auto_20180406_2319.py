# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0008_auto_20180406_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='log_user',
        ),
        migrations.AlterField(
            model_name='reports',
            name='event',
            field=models.CharField(max_length=200),
        ),
        migrations.DeleteModel(
            name='Log',
        ),
    ]
