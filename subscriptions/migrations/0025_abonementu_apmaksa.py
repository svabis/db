# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0014_blacklist_bl_user'),
        ('setup', '0004_apdrosinataji'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscriptions', '0024_abonementi_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Abonementu_Apmaksa',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('full_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('discount_price', models.DecimalField(max_digits=5, decimal_places=2)),
                ('deposit', models.BooleanField(default=False)),
                ('from_deposit', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gift_card', models.BooleanField(default=False)),
                ('from_gift_card', models.DecimalField(max_digits=5, decimal_places=2)),
                ('insurance_cash', models.DecimalField(max_digits=5, decimal_places=2)),
                ('cash', models.BooleanField(default=False)),
                ('card', models.BooleanField(default=False)),
                ('transfer', models.BooleanField(default=False)),
                ('addiitonal_discount', models.BooleanField(default=False)),
                ('total_ammount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('client', models.ForeignKey(to='clients.Klienti')),
                ('insurance', models.ForeignKey(blank=True, to='setup.Apdrosinataji', null=True)),
                ('subscr', models.ForeignKey(to='subscriptions.Abonementi')),
                ('user', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'abonementi_pirkums',
            },
        ),
    ]
