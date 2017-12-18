# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0007_auto_20171218_2315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timelimittype',
            old_name='name',
            new_name='title',
        ),
    ]
