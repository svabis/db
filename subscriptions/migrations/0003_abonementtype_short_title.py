# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0002_abonementi'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementtype',
            name='short_title',
            field=models.CharField(default=b'', max_length=60),
        ),
    ]
