from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import HealthDeclaration
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_healthdeclare(sender, instance, created, **kwards):
  if created:
    HealthDeclaration.objects.create(user=instance)

#post_save.connect(create_healthdeclare, sender=User)