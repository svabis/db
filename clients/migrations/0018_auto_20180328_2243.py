# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0017_deposit_d_remain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='reg_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
