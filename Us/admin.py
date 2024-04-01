from django.contrib import admin

from Us.models import AboutUs, SocialMedia, Message, Customer, TeamMember, WhatDoCustomersEarn, ModasOperandi


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
class ColleagueCompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "link")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role")


@admin.register(WhatDoCustomersEarn)
class WhatDoCustomersEarnAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(ModasOperandi)
class ModasOperandiAdmin(admin.ModelAdmin):
    list_display = ("title",)
