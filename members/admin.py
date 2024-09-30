from django.contrib import admin
from .models import anggota

# Register your models here.

class anggotaAdmin(admin.ModelAdmin):
  list_display = ("name", "penjuruan", "asal",)
  
admin.site.register(anggota, anggotaAdmin)