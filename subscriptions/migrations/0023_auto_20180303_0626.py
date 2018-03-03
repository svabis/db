# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0022_abonementtype_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonementtype',
            name='discount',
            field=models.BooleanField(default=True),
        ),
    ]
