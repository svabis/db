# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0003_auto_20180303_0515'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apdrosinataji',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('visible', models.BooleanField(default=False)),
                ('title', models.CharField(default=b'', max_length=40)),
            ],
            options={
                'db_table': 'apdrosinataji',
            },
        ),
    ]
