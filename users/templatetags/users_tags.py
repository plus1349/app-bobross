from django.conf import settings
from django.template import Library

register = Library()


@register.simple_tag(takes_context=True)
def get_languages(context):
    context['languages'] = settings.LANGUAGES
