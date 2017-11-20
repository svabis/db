# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0004_auto_20171120_1427'),
    ]

    operations = [
        migrations.AddField(
            model_name='klienti',
            name='avatar',
            field=models.ImageField(null=True, upload_to=b'client/', blank=True),
        ),
    ]
