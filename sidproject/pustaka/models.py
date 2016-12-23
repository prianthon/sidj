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
