from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class PaintingsConfig(AppConfig):
    name = 'paintings'
    verbose_name = _('Paintings')

    def ready(self):
        from . import signals
