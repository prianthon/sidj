from django.contrib import admin

from .models import Agama, GolonganDarah, HubunganKeluarga, JenisKelamin, Pekerjaan, Pendidikan

class AgamaAdmin(admin.ModelAdmin):
    list_display = ('id', 'agama')

class GolonganDarahAdmin(admin.ModelAdmin):
    list_display = ('id', 'golongan_darah')

class HubunganKeluargaAdmin(admin.ModelAdmin):
    list_display = ('id', 'hubungan_keluarga')

class JenisKelaminAdmin(admin.ModelAdmin):
    list_display = ('id', 'jenis_kelamin')

class PekerjaanAdmin(admin.ModelAdmin):
    list_display = ('id', 'pekerjaan', 'tipe')

class PendidikanAdmin(admin.ModelAdmin):
    list_display = ('id', 'pendidikan')

admin.site.register(Agama, AgamaAdmin)
admin.site.register(GolonganDarah, GolonganDarahAdmin)
admin.site.register(HubunganKeluarga, HubunganKeluargaAdmin)
admin.site.register(JenisKelamin, JenisKelaminAdmin)
admin.site.register(Pekerjaan, PekerjaanAdmin)
admin.site.register(Pendidikan, PendidikanAdmin)
