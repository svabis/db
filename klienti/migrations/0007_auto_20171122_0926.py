# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0006_auto_20171120_1707'),
    ]

    operations = [
        migrations.RenameField(
            model_name='klienti',
            old_name='sex',
            new_name='gender',
        ),
    ]
