# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0012_auto_20171126_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='name',
            field=models.CharField(default=b'', max_length=25),
        ),
        migrations.AlterField(
            model_name='klienti',
            name='surname',
            field=models.CharField(default=b'', max_length=25),
        ),
    ]
