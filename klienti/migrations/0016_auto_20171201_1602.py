# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('klienti', '0015_auto_20171126_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('status_name', models.CharField(default=b'', max_length=40)),
                ('status_discount', models.CharField(default=b'', max_length=5)),
            ],
            options={
                'db_table': 'status_type',
            },
        ),
        migrations.AlterField(
            model_name='klienti',
            name='status',
            field=models.ForeignKey(to='klienti.StatusType'),
        ),
    ]
