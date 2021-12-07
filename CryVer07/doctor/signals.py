from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MedicalRecord
from accounts.models import Patient
from django.contrib.auth.models import User

@receiver(post_save, sender=Patient)
def create_tc(sender, instance, created, **kwards):
  if created:
     MedicalRecord.objects.create(patient=instance)
#post_save.connect(create_tc, sender=Patient)