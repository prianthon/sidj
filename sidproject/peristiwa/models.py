from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

@python_2_unicode_compatible # mendukung Python 2
class Kelahiran(models.Model):
    # bayi yang lahir
    BAYI_KEMBARS = (
        ('YA', 'YA'),
        ('TIDAK', 'TIDAK'),
    )
    TEMPAT_KELAHIRANS = (
        ('Rumah Bersalin', 'Rumah Bersalin'),
        ('Bukan Rumah Bersalin', 'Bukan Rumah Bersalin'),
    )
    HUBUNGAN_PELAPOR_DENGAN_BAYIS = (
        ('Ayah', 'Ayah'),
        ('Ibu', 'Ibu'),
        ('Kakak', 'Kakak'),
        ('Kakek', 'Kakek'),
        ('Nenek', 'Nenek'),
        ('Paman', 'Paman'),
        ('Tante', 'Tante'),
        ('Keponakan', 'Keponakan'),
        ('Sepupu', 'Sepupu'),
        ('Kerabat', 'Kerabat'),
    )
    tanggal_dan_waktu_lahir = models.DateTimeField(default=timezone.now)
    nama_bayi = models.CharField(max_length=200)
    jenis_kelamin = models.ForeignKey('pustaka.JenisKelamin')
    berat_bayi = models.IntegerField()
    panjang_bayi = models.IntegerField()
    bayi_kembar = models.CharField(max_length=15, choices=BAYI_KEMBARS)
    anak_ini_lahir_yang_ke = models.IntegerField()
    tempat_kelahiran = models.CharField(max_length=30, choices=TEMPAT_KELAHIRANS)
    # desa kelahiran
    provinsi = models.CharField(max_length=100)
    kabupaten = models.CharField(max_length=100)
    kecamatan = models.CharField(max_length=100)
    desa_kelahiran = models.CharField(max_length=100)
    # Orangtua dari bayi
    nama_ibu = models.ForeignKey('penduduk.Penduduk')
    tanggal_nikah_ibu = models.DateField()
    nama_ayah = models.ForeignKey('penduduk.Penduduk')
    # pelapor peristiwa kelahiran
    nama_pelapor = models.ForeignKey('penduduk.Penduduk')
    hubungan_pelapor_dengan_bayi = models.CharField('max_length=15, choices=HUBUNGAN_PELAPOR_DENGAN_BAYIS')
    # saksi - saksi peristiwa kelahiran
    nama_saksi_1 = models.ForeignKey('penduduk.Penduduk')
    nama_saksi_2 = models.ForeignKey('penduduk.Penduduk')
