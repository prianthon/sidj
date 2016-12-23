from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible # mendukung Python 2
class Penduduk(models.Model):
    KEWARGANEGARAANS = (
        ('WNI', 'WNI'),
        ('WNA', 'WNA'),
        ('DWIKEWARGANEGARAAN', 'DWIKEWARGANEGARAAN'),
    )
    nik = models.CharField(max_length=20)
    nama = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=55)
    tanggal_lahir = models.DateField
    kewarganegaraan = models.CharField(max_length=50, choices=KEWARGANEGARAANS)
    foto = models.CharField(max_length=200)
    jenis_kelamin = models.ForeignKey('pustaka.JenisKelamin')
    golongan_darah = models.ForeignKey('pustaka.GolonganDarah')
    agama = models.ForeignKey('pustaka.Agama')
    status_kawin = models.ForeignKey('pustaka.StatusKawin')
    status_tinggal = models.ForeignKey('pustaka.StatusTinggal')
    pendidikan = models.ForeignKey('pustaka.Pendidikan')
    pekerjaan = models.ForeignKey('pustaka.Pekerjaan')
    nama_cacat = models.ForeignKey('pustaka.PenyandangCacat')
    status_kependudukan = models.ForeignKey('pustaka.StatusKependudukan')

    def __str__(self):
        return self.nik
