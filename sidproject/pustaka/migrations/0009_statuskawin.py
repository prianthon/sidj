# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pustaka', '0008_penyandangcacat'),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusKawin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_kawin', models.CharField(max_length=45)),
            ],
        ),
    ]
