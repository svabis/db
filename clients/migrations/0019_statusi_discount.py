# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0018_auto_20180328_2243'),
    ]

    operations = [
        migrations.AddField(
            model_name='statusi',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]
