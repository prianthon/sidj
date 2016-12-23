from django.contrib import admin

from .models import Agama, GolonganDarah, HubunganKeluarga, JenisKelamin, Pekerjaan, Pendidikan, PenyandangCacat, StatusKawin, StatusKependudukan, StatusKk, StatusTinggal

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

class PenyandangCacatAdmin(admin.ModelAdmin):
    list_display = ('id', 'nama_cacat', 'tipe_cacat')

class StatusKawinAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_kawin')

class StatusKependudukanAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_kependudukan')

class StatusKkAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_kk')

class StatusTinggalAdmin(admin.ModelAdmin):
    list_display = ('id', 'status_tinggal')

admin.site.register(Agama, AgamaAdmin)
admin.site.register(GolonganDarah, GolonganDarahAdmin)
admin.site.register(HubunganKeluarga, HubunganKeluargaAdmin)
admin.site.register(JenisKelamin, JenisKelaminAdmin)
admin.site.register(Pekerjaan, PekerjaanAdmin)
admin.site.register(Pendidikan, PendidikanAdmin)
admin.site.register(PenyandangCacat, PenyandangCacatAdmin)
admin.site.register(StatusKawin, StatusKawinAdmin)
admin.site.register(StatusKependudukan, StatusKependudukanAdmin)
admin.site.register(StatusKk, StatusKkAdmin)
admin.site.register(StatusTinggal, StatusTinggalAdmin)
