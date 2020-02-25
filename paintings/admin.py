from django.contrib.admin import register, ModelAdmin, TabularInline
from django.utils.translation import ugettext_lazy as _

from paintings.models import Category, Painting, PaintingLayer


# @register(Category)
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
        (None, {'fields': ('enabled', 'free')}),
        (_('Info'), {'fields': ('position', 'layers_count', 'title', 'size_name')}),
        (_('Files'), {'fields': ('image', 'archive')})
    )
    list_display = ('id', 'enabled', 'position', 'layers_count', 'title', 'size_name')
    list_display_links = ('id', 'title', 'size_name')
    list_editable = ('enabled', 'position', 'layers_count')
    list_filter = ('enabled', 'free', 'layers_count', 'size_name',)
    ordering = ('position', 'title', 'id')
    search_fields = ('title', )
