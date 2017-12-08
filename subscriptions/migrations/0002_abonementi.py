# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonementi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=60)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('purchase_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('active', models.BooleanField(default=True)),
                ('first_time', models.BooleanField(default=False)),
                ('best_before', models.DateTimeField(null=True, blank=True)),
                ('times', models.BooleanField(default=False)),
                ('times_count', models.IntegerField(null=True, blank=True)),
                ('client', models.ForeignKey(to='clients.Klienti')),
            ],
            options={
                'db_table': 'abonementi',
            },
        ),
    ]
