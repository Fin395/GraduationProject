from django.contrib import admin
from .models import PageCategory, Page

@admin.register(PageCategory)
class PageCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'page_category',)
    list_filter = ('name', 'page_category',)
    search_fields = ('name', 'description',)