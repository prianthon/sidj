from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible # mendukung Python 2
class PengaturanUmum(models.Model):
    nama_desa = models.CharField(max_length=100)
    kode_desa = models.CharField(max_length=100)
    nama_kepala_desa = models.CharField(max_length=100)
    nip_kepala_desa = models.CharField(max_length=100)
    kodepos = models.CharField(max_length=6)
    nama_kecamatan = models.CharField(max_length=100)
    kode_kecamatan = models.CharField(max_length=100)
    nama_kepala_camat = models.CharField(max_length=100)
    nip_kepala_camat = models.CharField(max_length=100)
    nama_kabupaten = models.CharField(max_length=100)
    kode_kabupaten = models.CharField(max_length=100)
    nama_provinsi = models.CharField(max_length=100)
    kode_provinsi = models.CharField(max_length=100)
    logo_desa = models.CharField(max_length=100)
    logo_kabupaten = models.CharField(max_length=100)
    alamat_kantor_desa = models.CharField(max_length=100)

    def __str__(self):
        return self.nama_desa
