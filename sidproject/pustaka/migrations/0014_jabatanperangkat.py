# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pustaka', '0013_libsurat'),
    ]

    operations = [
        migrations.CreateModel(
            name='JabatanPerangkat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_jabatan', models.CharField(max_length=100)),
            ],
        ),
    ]