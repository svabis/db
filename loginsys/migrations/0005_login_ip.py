# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0004_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='ip',
            field=models.CharField(default=b'', max_length=20),
        ),
    ]
