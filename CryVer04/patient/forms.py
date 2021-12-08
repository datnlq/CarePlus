from django.contrib.auth import get_user_model, models
from django import forms
from django.forms import fields
from doctor.models import MedicalRecord

from .models import KhaiBaoTrieuChung

class TrieuChungForm(forms.ModelForm):
  class Meta:
    model = KhaiBaoTrieuChung
    fields = [
      'TC1','TC2','TC3','TC4','TC5','TC6','TC7','TC8','TC9','TC10',
      'TC11','TC12','TC13','TC14','TC15','TC16','TC17','TC18','TC19',
      'TC20','TC21','TC22','TC23', 'Note'
    ]

