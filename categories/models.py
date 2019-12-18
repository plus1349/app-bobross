from django.db.models import BooleanField, CharField, Model, PositiveIntegerField
from django.utils.translation import ugettext_lazy as _


class Category(Model):
    enabled = BooleanField(_('enabled'), default=True)
    position = PositiveIntegerField(_('position'), blank=True, null=True)
    title = CharField(_('title'), max_length=255)

    class Meta:
        db_table = 'categories'
        ordering = ('position', 'title')
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    def __str__(self):
        return self.title

    @property
    def get_paintings(self):
        return self.paintings.filter(category=self, enabled=True, image__isnull=False)

    def save(self, *args, **kwargs):
        if self.position is None:
            self.position = self.id
        super().save(*args, **kwargs)
