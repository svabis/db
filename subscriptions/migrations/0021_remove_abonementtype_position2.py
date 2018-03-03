# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0020_auto_20180303_0205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abonementtype',
            name='position2',
        ),
    ]
