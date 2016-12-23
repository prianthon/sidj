# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-23 15:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pustaka', '0014_jabatanperangkat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Penduduk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nik', models.CharField(max_length=20)),
                ('nama', models.CharField(max_length=100)),
                ('tempat_lahir', models.CharField(max_length=55)),
                ('kewarganegaraan', models.CharField(choices=[('WNI', 'WNI'), ('WNA', 'WNA'), ('DWIKEWARGANEGARAAN', 'DWIKEWARGANEGARAAN')], max_length=50)),
                ('foto', models.CharField(max_length=200)),
                ('agama', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pustaka.Agama')),
                ('golongan_darah', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pustaka.GolonganDarah')),
                ('jenis_kelamin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pustaka.JenisKelamin')),
                ('nama_cacat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pustaka.PenyandangCacat')),
                ('pekerjaan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pustaka.Pekerjaan')),
                ('pendidikan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pustaka.Pendidikan')),
                ('status_kawin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pustaka.StatusKawin')),
                ('status_kependudukan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pustaka.StatusKependudukan')),
                ('status_tinggal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pustaka.StatusTinggal')),
            ],
        ),
    ]
