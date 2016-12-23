from django.contrib import admin

from .models import Agama, GolonganDarah, HubunganKeluarga, JenisKelamin

admin.site.register(Agama)
admin.site.register(GolonganDarah)
admin.site.register(HubunganKeluarga)
admin.site.register(JenisKelamin)
