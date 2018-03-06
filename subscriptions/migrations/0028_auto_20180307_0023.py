# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0027_auto_20180307_0021'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abonementu_apmaksa',
            old_name='total_ammount',
            new_name='final_price',
        ),
        migrations.RemoveField(
            model_name='abonementu_apmaksa',
            name='addiitonal_discount',
        ),
    ]
