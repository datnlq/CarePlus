from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import DateField
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from accounts.models import Patient

class MedicalRecord(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  m1=models.CharField(verbose_name=u"Loại thuốc 1", max_length=100, null=True, blank=True)
  m2=models.CharField(verbose_name=u"Loại thuốc 2", max_length=100, null=True, blank=True)
  m3=models.CharField(verbose_name=u"Loại thuốc 3", max_length=100, null=True, blank=True)
  m4=models.CharField(verbose_name=u"Loại thuốc 4", max_length=100, null=True, blank=True)
  m5=models.CharField(verbose_name=u"Loại thuốc 5", max_length=100, null=True, blank=True)
  m6=models.CharField(verbose_name=u"Loại thuốc 6", max_length=100, null=True, blank=True)
  m7=models.CharField(verbose_name=u"Loại thuốc 7", max_length=100, null=True, blank=True)
  m8=models.CharField(verbose_name=u"Loại thuốc 8", max_length=100, null=True, blank=True)
  m9=models.CharField(verbose_name=u"Loại thuốc 9", max_length=100, null=True, blank=True)
  m10=models.CharField(verbose_name=u"Loại thuốc 10", max_length=100, null=True, blank=True)
  d1 = models.CharField(verbose_name=u"Liều 1", max_length=100, null=True, blank=True)
  d2 = models.CharField(verbose_name=u"Liều 2", max_length=100, null=True, blank=True)
  d3 = models.CharField(verbose_name=u"Liều 3", max_length=100, null=True, blank=True)
  d4 = models.CharField(verbose_name=u"Liều 4", max_length=100, null=True, blank=True)
  d5 = models.CharField(verbose_name=u"Liều 5", max_length=100, null=True, blank=True)
  d6 = models.CharField(verbose_name=u"Liều 6", max_length=100, null=True, blank=True)
  d7 = models.CharField(verbose_name=u"Liều 7", max_length=100, null=True, blank=True)
  d8 = models.CharField(verbose_name=u"Liều 8", max_length=100, null=True, blank=True)
  d9 = models.CharField(verbose_name=u"Liều 9", max_length=100, null=True, blank=True)
  d10 = models.CharField(verbose_name=u"Liều 10", max_length=100, null=True, blank=True)
  note = models.TextField(verbose_name=u"Ghi chú", max_length=500, null=True, blank=True)

  def __str__(self):
    return '%s %s' % (self.patient.patientUser.user.first_name, self.patient.patientUser.user.last_name)

  
