# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0010_auto_20171126_0717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='e_mail',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
