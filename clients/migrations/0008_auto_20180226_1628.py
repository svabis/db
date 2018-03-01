# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_deposit_iesalde'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='StatusType',
            new_name='Statusi',
        ),
    ]
