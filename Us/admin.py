from django.contrib import admin

from Us.models import AboutUs, SocialMedia, Message, Customer, TeamMember, WhatDoCustomersEarn, ModasOperandi, Faq


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'mobile_phone', 'email', 'full_name', 'created_at']
    readonly_fields = ['user', 'mobile_phone', 'email', 'full_name']
    search_fields = ['user', 'mobile_phone', 'email', 'full_name']


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['__str__']


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Customer)
class CustomerCompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "link")
    prepopulated_fields = {'slug': ('name',)}


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


@admin.register(WhatDoCustomersEarn)
class WhatDoCustomersEarnAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(ModasOperandi)
class ModasOperandiAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("question",)

    prepopulated_fields = {"slug": ("question",)}
