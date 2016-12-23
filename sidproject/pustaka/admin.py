from django.contrib import admin

from .models import Agama, GolonganDarah, HubunganKeluarga, JenisKelamin, Pekerjaan

class PekerjaanAdmin(admin.ModelAdmin):
    list_display = ('id', 'pekerjaan', 'tipe')

admin.site.register(Agama)
admin.site.register(GolonganDarah)
admin.site.register(HubunganKeluarga)
admin.site.register(JenisKelamin)
admin.site.register(Pekerjaan, PekerjaanAdmin)
