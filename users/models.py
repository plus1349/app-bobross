from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import (
    CASCADE,
    BooleanField, CharField, DateTimeField, EmailField, ForeignKey,
    Model
)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager
from paintings.models import Painting, PaintingLayer


class User(AbstractBaseUser, PermissionsMixin):
    name = CharField(_('name'), blank=True, max_length=255)
    phone = CharField(_('phone'), blank=True, max_length=15)
    email = EmailField(_('email'), max_length=255, unique=True)
    is_staff = BooleanField(_('is staff'), default=False)
    date_joined = DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        ordering = ('is_superuser', 'id')
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return "User {pk}".format(pk=self.pk)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def paintings(self):
        return self.paintings.filter(user=self)


class UserPainting(Model):
    user = ForeignKey(User, null=True, on_delete=CASCADE, related_name='paintings', verbose_name=_('user'))
    painting = ForeignKey(
        Painting, null=True, on_delete=CASCADE,
        related_name='user_paintings', verbose_name=_('painting')
    )

    class Meta:
        db_table = 'user_paintings'
        ordering = ('id',)
        verbose_name = _('user painting')
        verbose_name_plural = _('user paintings')

    def __str__(self):
        return self.painting.title

    @property
    def layers(self):
        return self.layers.filter(user_painting=self)


class UserPaintingLayer(Model):
    finish = BooleanField(_('finish'), default=False)
    user_painting = ForeignKey(
        UserPainting, null=True, on_delete=CASCADE, related_name='layers', verbose_name=_('user painting')
    )
    painting_layer = ForeignKey(
        PaintingLayer, null=True, on_delete=CASCADE,
        related_name='user_painting_layers', verbose_name=_('painting layer')
    )

    class Meta:
        db_table = 'user_painting_layers'
        ordering = ('id',)
        verbose_name = _('user painting layer')
        verbose_name_plural = _('user painting layers')

    def __str__(self):
        return "{painting} layer {id}".format(painting=self.user_painting.painting.title, id=self.id)
