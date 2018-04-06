# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0020_remove_statusi_status_discount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='statusi',
            old_name='discount',
            new_name='status_discount',
        ),
    ]
