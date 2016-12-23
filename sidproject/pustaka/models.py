from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible # mendukung Python 2
class Agama(models.Model):
    agama = models.CharField(max_length=45)

    def __str__(self):
        return self.agama

@python_2_unicode_compatible # mendukung Python 2
class GolonganDarah(models.Model):
    golongan_darah = models.CharField(max_length=10)

    def __str__(self):
        return self.golongan_darah

@python_2_unicode_compatible # mendukung Python 2
class HubunganKeluarga(models.Model):
    hubungan_keluarga = models.CharField(max_length=45)

    def __str__(self):
        return self.hubungan_keluarga

@python_2_unicode_compatible # mendukung Python 2
class JenisKelamin(models.Model):
    jenis_kelamin = models.CharField(max_length=45)

    def __str__(self):
        return self.jenis_kelamin

@python_2_unicode_compatible # mendukung Python 2
class Pekerjaan(models.Model):
    TIPES = (
        ('A', 'A untuk PNS dan Mandiri'),
        ('B', 'B untuk Sebaliknya'),
    )
    pekerjaan = models.CharField(max_length=75)
    tipe = models.CharField(max_length=1, choices=TIPES)

    def __str__(self):
        return self.pekerjaan

@python_2_unicode_compatible # mendukung Python 2
class Pendidikan(models.Model):
    pendidikan = models.CharField(max_length=75)

    def __str__(self):
        return self.pendidikan

@python_2_unicode_compatible # mendukung Python 2
class PenyandangCacat(models.Model):
    TIPE_CACATS = (
        ('FISIK', 'FISIK'),
        ('MENTAL', 'MENTAL'),
        ('NULL', 'NULL'),
    )
    nama_cacat = models.CharField(max_length=45)
    tipe_cacat = models.CharField(max_length=15, choices=TIPE_CACATS)

    def __str__(self):
        return self.nama_cacat

@python_2_unicode_compatible # mendukung Python 2
class StatusKawin(models.Model):
    status_kawin = models.CharField(max_length=45)

    def __str__(self):
        return self.status_kawin

@python_2_unicode_compatible # mendukung Python 2
class StatusKependudukan(models.Model):
    status_kependudukan = models.CharField(max_length=45)

    def __str__(self):
        return self.status_kependudukan

@python_2_unicode_compatible # mendukung Python 2
class StatusKk(models.Model):
    status_kk = models.CharField(max_length=64)

    def __str__(self):
        return self.status_kk

@python_2_unicode_compatible # mendukung Python 2
class StatusTinggal(models.Model):
    status_tinggal = models.CharField(max_length=45)

    def __str__(self):
        return self.status_tinggal

@python_2_unicode_compatible # mendukung Python 2
class LibSurat(models.Model):
    kode_surat = models.CharField(max_length=45, primary_key=True)
    nama_surat = models.CharField(max_length=200)
    parent_id = models.CharField(max_length=45)

    def __str__(self):
        return self.nama_surat
