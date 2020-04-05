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
        (_('Files'), {'fields': ('thumnail', 'image', 'archive')})
    )
    list_display = ('id', 'enabled', 'position', 'title')
    list_display_links = ('id', 'title')
    list_editable = ('enabled', 'position')
    list_filter = ('enabled', 'free')
    ordering = ('position', 'title', 'id')
    readonly_fields = ('thumnail',)
    search_fields = ('title',)

    class Media:
        css = {'all': ('css/custom.css',)}

    @staticmethod
    def thumnail(instance):
        if instance.image:
            return mark_safe(
                """
                <a target="_blank" href="{src}">
                  <img alt="{alt}" src="{src}" class="thumbnail">
                </a>
                """.format(alt=instance.title, src=instance.image.url)
            )
        return str()
