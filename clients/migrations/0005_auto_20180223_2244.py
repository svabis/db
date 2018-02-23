# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_remove_klienti_empty_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='notes',
            field=models.CharField(default=b'', max_length=500, blank=True),
        ),
    ]
