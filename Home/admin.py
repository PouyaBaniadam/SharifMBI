from django.contrib import admin

from Home.models import HeroBanner


@admin.register(HeroBanner)
class HeroBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "can_be_shown")

    list_editable = ("can_be_shown",)
