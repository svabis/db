# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Abonementi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=40)),
                ('price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('active', models.BooleanField(default=True)),
                ('first_time', models.BooleanField(default=False)),
                ('best_before', models.CharField(max_length=2, null=True, blank=True)),
                ('time_limit', models.BooleanField(default=False)),
                ('times', models.BooleanField(default=False)),
                ('times_count', models.IntegerField(null=True, blank=True)),
            ],
            options={
                'db_table': 'abonementi',
            },
        ),
    ]
