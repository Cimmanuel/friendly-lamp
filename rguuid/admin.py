from django.contrib import admin

from .models import RGUUID


@admin.register(RGUUID)
class RGUUIDAdmin(admin.ModelAdmin):
    list_display = ["id", "created"]
