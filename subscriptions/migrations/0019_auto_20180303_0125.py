# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0018_auto_20180302_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abonementtype',
            name='short_title',
            field=models.CharField(default=b'', max_length=100),
        ),
        migrations.AlterField(
            model_name='abonementtype',
            name='title',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
