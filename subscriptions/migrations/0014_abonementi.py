# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0006_klienti_first'),
        ('subscriptions', '0013_auto_20180224_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonementi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=False)),
                ('ended', models.BooleanField(default=False)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('purchase_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('activation_date', models.DateTimeField(null=True, blank=True)),
                ('activate_before', models.DateTimeField(null=True, blank=True)),
                ('best_before', models.DateTimeField(null=True, blank=True)),
                ('times_count', models.IntegerField(null=True, blank=True)),
                ('client', models.ForeignKey(to='clients.Klienti')),
                ('subscr', models.ForeignKey(to='subscriptions.AbonementType')),
            ],
            options={
                'db_table': 'abonementi',
            },
        ),
    ]
