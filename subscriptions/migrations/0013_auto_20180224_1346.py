# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0012_abonementtype_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='abonementi',
            name='client',
        ),
        migrations.DeleteModel(
            name='Abonementi',
        ),
    ]
