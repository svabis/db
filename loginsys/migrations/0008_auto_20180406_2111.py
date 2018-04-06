# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0007_remove_reports_ip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reports',
            name='event',
            field=models.CharField(max_length=50),
        ),
    ]
