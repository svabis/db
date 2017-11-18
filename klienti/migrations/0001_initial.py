# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klienti',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'', max_length=15)),
                ('surname', models.CharField(default=b'', max_length=15)),
                ('birthday', models.DateTimeField(default=django.utils.timezone.now)),
                ('phone', models.CharField(default=b'', max_length=16)),
                ('e_mail', models.EmailField(max_length=254)),
                ('card_nr', models.CharField(default=b'', max_length=16)),
                ('status', models.CharField(max_length=1, choices=[(b'B', b'Biedrs'), (b'S', b'Sudrabs'), (b'Z', b'Zelts'), (b'V', b'Vip'), (b'D', b'Darbinieks')])),
                ('sex', models.CharField(max_length=1, choices=[(b'V', b'V\xc4\xabrietis'), (b'S', b'Sieviete')])),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('notes', models.CharField(default=b'', max_length=150)),
            ],
            options={
                'db_table': 'klienti',
            },
        ),
    ]
