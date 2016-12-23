# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 04:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pustaka', '0007_pendidikan'),
    ]

    operations = [
        migrations.CreateModel(
            name='PenyandangCacat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_cacat', models.CharField(max_length=45)),
                ('tipe_cacat', models.CharField(choices=[('FISIK', 'FISIK'), ('MENTAL', 'MENTAL'), ('NULL', 'NULL')], max_length=15)),
            ],
        ),
    ]
