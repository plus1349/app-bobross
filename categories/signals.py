from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Category


@receiver(post_save, sender=Category)
def category_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.position is None:
            instance.position = instance.id
            instance.save(update_fields=('position',))
