from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class CategoriesConfig(AppConfig):
    name = 'categories'
    verbose_name = _('Categories')

    def ready(self):
        from . import signals
