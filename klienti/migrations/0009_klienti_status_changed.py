# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0008_klienti_society'),
    ]

    operations = [
        migrations.AddField(
            model_name='klienti',
            name='status_changed',
            field=models.BooleanField(default=False),
        ),
    ]
