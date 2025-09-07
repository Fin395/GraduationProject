from django.contrib import admin
from .models import Page, Section


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')
    search_fields = ('name',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'page', 'owner')
    search_fields = ('name', 'page')
    list_filter = ('page',)

