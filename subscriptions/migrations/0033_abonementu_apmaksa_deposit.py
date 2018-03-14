# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0017_deposit_d_remain'),
        ('subscriptions', '0032_auto_20180313_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='abonementu_apmaksa',
            name='deposit',
            field=models.ForeignKey(blank=True, to='clients.Deposit', null=True),
        ),
    ]
