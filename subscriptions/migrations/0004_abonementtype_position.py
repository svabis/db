# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0003_abonementtype_short_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementtype',
            name='position',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
