from django.contrib import admin
from .models import Profile, Skill, Message


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'email', 'short_intro', 'location')
    list_display_links = ('name', 'username')
    list_per_page = 25


class SkillAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
    list_display_links = ('name',)
    list_per_page = 25


class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipient', 'name', 'subject')
    list_display_links = ('name',)
    list_per_page = 25


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Message, MessageAdmin)
