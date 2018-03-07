# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_auto_20180307_2223'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deposit',
            old_name='d_amount',
            new_name='d_added',
        ),
    ]
