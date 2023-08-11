from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Device._meta.fields]


@admin.register(DeviceLog)
class DeviceLogAdmin(admin.ModelAdmin):
    list_display = [field.name for field in DeviceLog._meta.fields]
