from django.contrib.admin import register, ModelAdmin, TabularInline
from django.utils.html import mark_safe
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
        (_('Info'), {'fields': ('position', 'title')}),
        (_('Files'), {'fields': ('preview', 'image', 'archive')})
    )
    list_display = ('id', 'enabled', 'position', 'title')
    list_display_links = ('id', 'title')
    list_editable = ('enabled', 'position')
    list_filter = ('enabled', 'free')
    ordering = ('position', 'title', 'id')
    readonly_fields = ('preview',)
    search_fields = ('title', )

    @staticmethod
    def preview(instance):
        if instance.image:
            return mark_safe('<img src="{src}" width="150" />'.format(src=instance.image.url))
