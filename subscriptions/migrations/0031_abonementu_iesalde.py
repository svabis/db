# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0017_deposit_d_remain'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0030_auto_20180307_2331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonementu_Iesalde',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('activate_before', models.DateTimeField(null=True, blank=True)),
                ('best_before', models.DateTimeField(null=True, blank=True)),
                ('client', models.ForeignKey(to='clients.Klienti')),
                ('subscr', models.ForeignKey(to='subscriptions.Abonementi')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'abonementi_iesalde',
            },
        ),
    ]
