from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Account, Doctor
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwards):
  if created:
     Account.objects.create(user=instance)
     print('Profile created!')

#post_save.connect(create_profile, sender=User)
@receiver(post_save, sender=User)
def update_profile(sender, instance, created, **kwards):
  if created:
      instance.profile.save()
      print('Profile updated!')

#post_save.connect(update_profile, sender=User)

@receiver(post_save, sender=Account)
def create_doctor(sender, instance:Account, **kwards):
  qs = Doctor.objects.filter(doctorUser=instance)
  if instance.type_account == "Bác sĩ" and not qs.exists():
    Doctor.objects.create(doctorUser=instance)
#post_save.connect(create_doctor, sender=Account)