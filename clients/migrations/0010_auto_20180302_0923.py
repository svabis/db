# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20180226_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='klienti',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='klienti',
            name='disabled_until',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='klienti',
            name='elderly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='klienti',
            name='student',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='klienti',
            name='student_until',
            field=models.DateField(null=True, blank=True),
        ),
    ]
