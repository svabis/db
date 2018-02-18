# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_klienti_empty_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bl_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('bl_data', models.CharField(max_length=300)),
                ('bl_user', models.ForeignKey(to='clients.Klienti')),
            ],
            options={
                'db_table': 'blacklist',
            },
        ),
    ]
