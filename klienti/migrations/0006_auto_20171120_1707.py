# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0005_klienti_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='klienti',
            name='card_nr',
            field=models.CharField(default=b'', max_length=16, blank=True),
        ),
        migrations.AlterField(
            model_name='klienti',
            name='status',
            field=models.CharField(max_length=1, choices=[(b'B', b'Biedrs'), (b'S', b'Sudrabs'), (b'Z', b'Zelts'), (b'V', b'VIP'), (b'D', b'Darbinieks')]),
        ),
    ]
