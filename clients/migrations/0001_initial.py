# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klienti',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('s3_nr', models.CharField(default=b'', max_length=10)),
                ('name', models.CharField(default=b'', max_length=40)),
                ('surname', models.CharField(default=b'', max_length=40)),
                ('avatar', models.ImageField(null=True, upload_to=b'client/', blank=True)),
                ('birthday', models.DateField(null=True, blank=True)),
                ('phone', models.CharField(max_length=25, null=True, blank=True)),
                ('e_mail', models.EmailField(max_length=254, null=True, blank=True)),
                ('card_nr', models.CharField(default=b'', max_length=16, blank=True)),
                ('card_blocked', models.BooleanField(default=False)),
                ('client_blocked', models.BooleanField(default=False)),
                ('status_changed', models.BooleanField(default=False)),
                ('society', models.BooleanField(default=False)),
                ('gender', models.CharField(max_length=1, choices=[(b'V', b'V\xc4\xabrietis'), (b'S', b'Sieviete')])),
                ('reg_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('notes', models.CharField(default=b'', max_length=150, blank=True)),
            ],
            options={
                'db_table': 'klienti',
            },
        ),
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
        migrations.AddField(
            model_name='klienti',
            name='status',
            field=models.ForeignKey(to='clients.StatusType'),
        ),
    ]
