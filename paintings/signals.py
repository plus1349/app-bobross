from django.db.models.signals import post_save
from django.dispatch import receiver

from paintings.models import Painting, PaintingLayer


@receiver(post_save, sender=Painting)
def painting_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.position is None:
            instance.position = instance.id
            instance.save(update_fields=('position',))


@receiver(post_save, sender=PaintingLayer)
def painting_layer_post_save(sender, instance, created, **kwargs):
    if created:
        if instance.position is None:
            instance.position = instance.id
            instance.save(update_fields=('position',))
