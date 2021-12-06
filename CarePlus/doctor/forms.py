from django.contrib.auth import get_user_model
from django import forms

from accounts.models import Account, Patient

User = get_user_model()

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

  