from django.contrib import admin

from Diagnose.models import Diagnose


@admin.register(Diagnose)
class DiagnoseAdmin(admin.ModelAdmin):
    list_display = ('user', "file", "uploaded_at")
