# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0009_klienti_status_changed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='birthday',
            field=models.DateField(null=True, blank=True),
        ),
    ]
