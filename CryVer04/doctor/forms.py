from django.contrib.auth import get_user_model, models
from django import forms
from django.forms import fields
from django.contrib.auth.models import User
from django.forms.forms import Form
from accounts.models import Account, Patient
from doctor.models import MedicalRecord
from patient.models import DanhGia, KhaiBaoTrieuChung


class AddPatient(forms.Form):
  CMND = forms.CharField(label="CMND", widget=forms.TextInput(attrs={'class':'form-control'}))

  def clean_CMND(self):
    CMND = self.cleaned_data.get("CMND")
    qs = Account.objects.filter(CMND__exact=CMND)
    print(qs)
    if not qs.exists():
      raise forms.ValidationError("Không tồn tại CMND phù hợp.")
    else:
      ws = Account.objects.get(CMND__exact=CMND)
      ws_check = Patient.objects.filter(patientUser=ws)
      if ws_check.exists():
        raise forms.ValidationError("Bạn đã thêm bệnh nhân này vào rồi!")
    return CMND

class PatientDetailForm(forms.ModelForm):
  class Meta:
    model = Patient
    fields = [
      'NgayPhatBenh',
      'LyDo',
      'SDTNguoiThan',
      'BenhNen',
      'NoiDiQua',
      'TinhTrang',
      'Note'
    ]

class DanhGiaTrieuChung(forms.ModelForm):
  class Meta:
    model = DanhGia
    fields = ['DanhGia']

class MedicalRecordUpdate(forms.ModelForm):
  class Meta:
    model = MedicalRecord
    fields = [
      'note',
      'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9', 'm10', 
      'd1','d2','d3','d4','d5','d6','d7','d8','d9','d10',
    ]
