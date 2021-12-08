from django.shortcuts import render
from accounts.models import Patient
from doctor.models import MedicalRecord
from patient.forms import TrieuChungForm, PatientUpdateForm
from .models import KhaiBaoTrieuChung
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def tc_update(request):
  patient_id = Patient.objects.filter(patientUser=request.user.profile).values('pk').get()
  patient = Patient.objects.get(id=patient_id['pk'])
  tc_id = KhaiBaoTrieuChung.objects.filter(patient=patient).values('pk').get()
  tc = KhaiBaoTrieuChung.objects.get(id=tc_id['pk'])

  if request.method=='POST':
    form = TrieuChungForm(request.POST, instance=tc)
    if form.is_valid():
      form.save()
      messages.success(request, 'Đã thay đổi khai báo triệu chứng của bạn! Bác sĩ sẽ xem sớm và kê đơn thuốc.')
  else:
    form = TrieuChungForm(instance=tc)
  context = {
    'form': form,
  }
  return render(request,'patient/trieuchung_update.html', context)

@login_required(login_url="login")
def medical_view(request):
  patient_id = Patient.objects.filter(patientUser=request.user.profile).values('pk').get()
  patient = Patient.objects.get(id=patient_id['pk'])
  medical_id = MedicalRecord.objects.filter(patient=patient).values('pk').get()
  medicals = MedicalRecord.objects.filter(id=medical_id['pk']).values().get()
  #region Medial
  m1 = medicals['m1']
  m2 = medicals['m2']
  m3 = medicals['m3']
  m4 = medicals['m4']
  m5 = medicals['m5']
  m6 = medicals['m6']
  m7 = medicals['m7']
  m8 = medicals['m8']
  m9 = medicals['m9']
  m10 = medicals['m10']

  d1 = medicals['d1']
  d2 = medicals['d2']
  d3 = medicals['d3']
  d4 = medicals['d4']
  d5 = medicals['d5']
  d6 = medicals['d6']
  d7 = medicals['d7']
  d8 = medicals['d8']
  d9 = medicals['d9']
  d10 = medicals['d10']

  note = medicals['note']
  #endregion
  
  context={
    'm1':m1, 'm2':m2,'m3':m3,'m4':m4,'m5':m5,'m6':m6,'m7':m7,'m8':m8,'m9':m9,'m10':m10,
    'd1':d1, 'd2':d2, 'd3':d3, 'd4':d4, 'd5':d5, 'd6':d6, 'd7':d7, 'd8':d8, 'd9':d9, 'd10':d10,
    'note':note,
  }

  return render(request,'patient/medical_record.html', context) 

@login_required(login_url="login")
def patient_update2(request):
  patient_id = Patient.objects.filter(patientUser=request.user.profile).values('pk').get()
  patient = Patient.objects.get(id=patient_id['pk'])
  
  if request.method=='POST':
    form_patient = PatientUpdateForm(request.POST, instance=patient)

    if form_patient.is_valid():
      form_patient.save()

      messages.success(request, 'Cập nhật bệnh án thành công!')
  else:
    form_patient = PatientUpdateForm(instance=patient)

  context = {
    'form_patient': form_patient,
  }
  return render(request,'base/patient_update.html', context)
