from django.db import models
from django.db.models import BooleanField, CharField, Model, PositiveIntegerField
from django.utils.translation import ugettext_lazy as _


class Category(Model):
    enabled = BooleanField(_('enabled'), default=True)
    position = PositiveIntegerField(_('position'), db_index=True, editable=False)
    title = CharField(_('title'), max_length=255)

    class Meta:
        db_table = 'categories'
        ordering = ('position', 'title',)
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title

    # @property
    # def get_translations(self):
    #     return self.translations.filter(category=self)


# class CategoryTranslation(models.Model):
#     category = models.ForeignKey(
#         Category, blank=True, null=True, on_delete=models.SET_NULL,
#         related_name='translations', verbose_name=_('category')
#     )
#     title = models.CharField(_('title'), max_length=255)
#     locale = models.CharField(_('locale'), max_length=2)
#
#     class Meta:
#         ordering = ('-title',)
#         verbose_name = _('category translation')
#         verbose_name_plural = _('category translations')
#
#     def __str__(self):
#         return self.title
