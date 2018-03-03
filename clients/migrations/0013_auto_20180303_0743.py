# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clients', '0012_auto_20180303_0337'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='iesalde',
            name='i_client',
        ),
        migrations.RenameField(
            model_name='blacklist',
            old_name='bl_user',
            new_name='bl_client',
        ),
        migrations.AddField(
            model_name='deposit',
            name='d_user',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Iesalde',
        ),
    ]
