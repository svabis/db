# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0011_auto_20171219_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementtype',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
