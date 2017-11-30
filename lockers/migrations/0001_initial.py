# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0015_auto_20171126_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skapji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=3)),
                ('locker_type', models.CharField(max_length=1, choices=[(b'V', b'V\xc4\xabrietis'), (b'S', b'Sieviete')])),
                ('checkin_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('client', models.ForeignKey(related_name='locker_client', to='klienti.Klienti')),
            ],
            options={
                'db_table': 'skapji',
            },
        ),
    ]
