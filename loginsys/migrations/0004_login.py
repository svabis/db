# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('loginsys', '0003_auto_20180215_1403'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('event', models.CharField(max_length=10)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_autorization',
            },
        ),
    ]
