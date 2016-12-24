from django.contrib import admin

from .models import Kelahiran

#class KelahiranAdmin(admin.ModelAdmin):
#    fieldsets = [
#        ('Bayi yang Lahir', {'fields': ['tanggal_dan_waktu_lahir', '']})
#    ]

admin.site.register(Kelahiran)
