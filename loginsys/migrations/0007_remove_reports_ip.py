# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0006_reports'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reports',
            name='ip',
        ),
    ]
