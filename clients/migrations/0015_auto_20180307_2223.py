# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_blacklist_bl_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='deposit',
            name='d_reason',
            field=models.CharField(default=b'', max_length=150, blank=True),
        ),
        migrations.AlterField(
            model_name='klienti',
            name='notes',
            field=models.CharField(default=b'', max_length=1000, blank=True),
        ),
    ]
