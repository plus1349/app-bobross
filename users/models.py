from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db.models import BooleanField, CharField, DateTimeField, EmailField, FileField, ForeignKey, Model, CASCADE
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from bobross.utils import file_directory
from paintings.models import Painting, PaintingLayer
from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    name = CharField(_('name'), blank=True, max_length=255)
    phone = CharField(_('phone'), blank=True, max_length=15)
    email = EmailField(_('email'), max_length=255, unique=True)
    device_id = CharField(_('device id'), null=True, max_length=255, unique=True)
    is_staff = BooleanField(_('is staff'), default=False)
    date_joined = DateTimeField(_('date joined'), default=timezone.now)
    state = FileField(_('state'), blank=True, null=True, upload_to=file_directory)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'users'
        ordering = ('-is_superuser', '-is_staff', 'id')
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def __str__(self):
        return "User {pk}".format(pk=self.pk)

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    @property
    def file_directory(self):
        return 'users/states/'

    @property
    def paintings(self):
        return self.paintings.filter(user=self)


class UserPainting(Model):
    user = ForeignKey(User, null=True, on_delete=CASCADE, related_name='paintings', verbose_name=_('user'))
    painting = ForeignKey(
        Painting, null=True, on_delete=CASCADE,
        related_name='user_paintings', verbose_name=_('painting')
    )
    progress = FileField(_('progress'), null=True, upload_to=file_directory)

    class Meta:
        db_table = 'user_paintings'
        ordering = ('id',)
        unique_together = ('user', 'painting')
        verbose_name = _('user painting')
        verbose_name_plural = _('user paintings')

    def __str__(self):
        return self.painting.title

    @property
    def file_directory(self):
        return 'users/paintings/progress/'

    @property
    def finish(self):
        finish = all([layer.finish for layer in self.get_layers.all()])
        return finish

    @property
    def get_layers(self):
        return self.layers.filter(user_painting=self)


class UserPaintingLayer(Model):
    finish = BooleanField(_('finish'), default=False)
    user_painting = ForeignKey(
        UserPainting, null=True, on_delete=CASCADE,
        related_name='layers', verbose_name=_('user painting')
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
        return "{painting} layer {id}".format(
            painting=self.user_painting.painting.title, id=self.painting_layer.position
        )
