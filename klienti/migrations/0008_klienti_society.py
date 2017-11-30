# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0007_auto_20171122_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='klienti',
            name='society',
            field=models.BooleanField(default=False),
        ),
    ]
