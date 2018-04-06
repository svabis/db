# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0019_statusi_discount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='statusi',
            name='status_discount',
        ),
    ]
