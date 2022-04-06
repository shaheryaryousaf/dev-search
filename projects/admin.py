from django.contrib import admin

from projects.views import editProject
from .models import Project, Review, Tag


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'vote_total', 'created_at')
    list_display_links = ('title',)
    list_editable = ('vote_total', 'user')
    list_per_page = 25


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('project', 'user', 'value', 'created_at')
    list_display_links = ('project',)
    list_per_page = 25


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    list_per_page = 25


admin.site.register(Project, ProjectAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Tag, TagAdmin)
