from django.contrib import admin
from .models import Page, Section


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'page',)
    search_fields = ('name', 'page')
    list_filter = ('page',)

