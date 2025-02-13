from django.db.models import (
    BooleanField, CharField, FileField, ForeignKey, ImageField, PositiveIntegerField, Model, CASCADE, SET_NULL
)
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from bobross.utils import image_directory, file_directory


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


class Painting(Model):
    enabled = BooleanField(_('enabled'), default=True)
    free = BooleanField(_('free'), default=False)
    position = PositiveIntegerField(_('position'), blank=True, null=True)
    category = ForeignKey(
        Category, blank=True, null=True, on_delete=SET_NULL,
        related_name='paintings', verbose_name=_('category')
    )
    title = CharField(_('title'), null=True, max_length=255)
    image = ImageField(_('image'), null=True, upload_to=image_directory)
    archive = FileField(_('archive'), null=True, upload_to=file_directory)
    layers_count = PositiveIntegerField(_('layers count'), null=True)
    size_name = CharField(_('size name'), null=True, max_length=55)

    class Meta:
        db_table = 'paintings'
        verbose_name = _('painting')
        verbose_name_plural = _('paintings')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('painting_retrieve', args=(self.id,))

    @property
    def file_directory(self):
        return 'paintings/archives/'

    @property
    def image_directory(self):
        return 'paintings/images/'

    @property
    def layers(self):
        return self.layers.filter(image__isnull=False, painting=self)

    def save(self, *args, **kwargs):
        if self.position is None:
            self.position = self.id
        super().save(*args, **kwargs)


class PaintingLayer(Model):
    position = PositiveIntegerField(_('position'), blank=True, null=True)
    painting = ForeignKey(Painting, null=True, on_delete=CASCADE, related_name='layers', verbose_name=_('painting'))
    image = ImageField(_('image'), null=True, upload_to=image_directory)

    class Meta:
        db_table = 'painting_layers'
        ordering = ('painting', 'position',)
        verbose_name = _('painting layer')
        verbose_name_plural = _('painting layers')

    def __str__(self):
        return "{painting} layer {position}".format(painting=self.painting.title, position=self.position)

    @property
    def file_directory(self):
        return 'paintings/layers/images/'

    def save(self, *args, **kwargs):
        if self.position is None:
            self.position = self.id
        super().save(*args, **kwargs)
