from django.contrib.admin import register, ModelAdmin, TabularInline
from .models import Category, Painting, PaintingLayer


@register(Category)
class CategoryAdmin(ModelAdmin):
    list_display = ('id', 'enabled', 'position', 'title')
    list_display_links = ('title',)
    list_editable = ('enabled', 'position')


class PaintingLayerAdmin(TabularInline):
    model = PaintingLayer
    extra = 0
    classes = ('collapse',)


@register(Painting)
class PaintingAdmin(ModelAdmin):
    fieldsets = (
        (None, {'fields': ('enabled', 'free', 'position', 'category', 'title', 'image')}),
    )
    inlines = (PaintingLayerAdmin,)
    list_display = ('id', 'enabled', 'category', 'position', 'title')
    list_display_links = ('title',)
    list_editable = ('enabled', 'position')
    list_filter = ('category',)
    ordering = ('category', 'position', 'title')
