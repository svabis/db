# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_auto_20171208_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonementi',
            name='title',
            field=models.CharField(default=b'', max_length=60),
        ),
    ]
