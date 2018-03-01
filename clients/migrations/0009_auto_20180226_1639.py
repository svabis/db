# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_auto_20180226_1628'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deposit',
            name='d_used',
        ),
        migrations.RemoveField(
            model_name='iesalde',
            name='i_used',
        ),
    ]
