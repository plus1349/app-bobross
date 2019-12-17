from django.contrib import admin

from .models import Category


# class CategoryTranslationAdmin(admin.TabularInline):
#     model = CategoryTranslation
#     extra = 0
#     classes = ('collapse',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # inlines = (CategoryTranslationAdmin,)
    list_editable = ('enabled',)
    list_display = ('enabled', 'title')
    list_display_links = ('title',)
