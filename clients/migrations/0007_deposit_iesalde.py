# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_klienti_first'),
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('d_used', models.BooleanField(default=False)),
                ('d_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('d_amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('d_client', models.ForeignKey(to='clients.Klienti')),
            ],
            options={
                'db_table': 'depozits',
            },
        ),
        migrations.CreateModel(
            name='Iesalde',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('i_used', models.BooleanField(default=False)),
                ('i_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('i_amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('i_client', models.ForeignKey(to='clients.Klienti')),
            ],
            options={
                'db_table': 'iesalde',
            },
        ),
    ]
