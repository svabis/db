# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0021_remove_abonementtype_position2'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementtype',
            name='discount',
            field=models.BooleanField(default=False),
        ),
    ]
