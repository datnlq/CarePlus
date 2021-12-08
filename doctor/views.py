#region Module
from django import forms
from django.contrib.auth import get_user_model
from accounts.models import Account, Doctor, Patient
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.timezone import datetime
from django.contrib.auth.decorators import login_required

from doctor.forms import AddPatient, DanhGiaTrieuChung, MedicalRecordUpdate, PatientDetailForm
from patient.models import DanhGia
from django.contrib.auth.models import User

from doctor.models import MedicalRecord
from patient.models import KhaiBaoTrieuChung
#endregion

class PatientHome(LoginRequiredMixin,ListView):
  model = Patient
  context_object_name = 'patient_home'
  template_name = 'base/patient_home.html'

  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    profile = Account.objects.get(user__exact=self.request.user)
    doctor = Doctor.objects.get(doctorUser__exact=profile)
    context['patient_home'] = Patient.objects.filter(doctorUser=doctor).filter(TinhTrang="Đang điều trị tại nhà").order_by('-id')
    context['count_home'] = context['patient_home'].count()
    return context

class PatientHospital(LoginRequiredMixin,ListView):
  model = Patient
  context_object_name = 'patient_hospital'
  template_name = 'base/patient_hospital.html'

  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    profile = Account.objects.get(user__exact=self.request.user)
    doctor = Doctor.objects.get(doctorUser__exact=profile)
    context['patient_hospital'] = Patient.objects.filter(doctorUser=doctor).filter(TinhTrang="Đã nhập viện").order_by('-id')
    context['count_hospital'] = context['patient_hospital'].count()
    return context

class PatientOK(LoginRequiredMixin,ListView):
  model = Patient
  context_object_name = 'patient_ok'
  template_name = 'base/patient_ok.html'

  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    profile = Account.objects.get(user__exact=self.request.user)
    doctor = Doctor.objects.get(doctorUser__exact=profile)
    context['patient_ok'] = Patient.objects.filter(doctorUser=doctor).filter(TinhTrang="Đã khỏi bệnh").order_by('-id')
    context['count_ok'] = context['patient_ok'].filter(TinhTrang="Đã khỏi bệnh").count()
    return context

@login_required(login_url="login")
def add_patient(request):
  add_form = AddPatient(request.POST or None)
  if add_form.is_valid():
    CMND = add_form.cleaned_data.get("CMND") 
    try:
      patientUser = Account.objects.filter(CMND=CMND).values('pk').get()
      doctorUser = Account.objects.filter(user=request.user).values('pk').get()
      patient = Patient.objects.create(patientUser_id=patientUser['pk'], doctorUser_id=doctorUser['pk'])
      patient.save()
      messages.success(request, "Bạn đã thêm bệnh nhân thành công vào danh sách điều trị tại nhà!")
    except:
      patient = None
    if patient != None:
      return redirect("addpatient")
    else:
      request.session['patient_error'] = 1 #1==True
  return render(request, 'base/add_patient.html', {'add_form': add_form})

@login_required(login_url="login")
def patient_update(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  
  patient_id = Patient.objects.filter(id=patient_id).values('patientUser_id').get()
  patient_profile = Account.objects.filter(id=patient_id['patientUser_id']).values('user_id').get()
  first_name = User.objects.filter(id=patient_profile['user_id']).values('first_name').get()
  last_name = User.objects.filter(id=patient_profile['user_id']).values('last_name').get()
  name = first_name['first_name'] + " " + last_name['last_name']
  
  if request.method=='POST':
    form_patient = PatientDetailForm(request.POST, instance=patient)

    if form_patient.is_valid():
      form_patient.save()

      messages.success(request, 'Cập nhật bệnh án thành công!')
  else:
    form_patient = PatientDetailForm(instance=patient)

  context = {
    'form_patient': form_patient,
    'name': name,
  }
  return render(request,'base/patient_update.html', context)

@login_required(login_url="login")
def trieuchung_update(request, patient_id):
  patient = Patient.objects.get(id=patient_id)

  patient_tc_id = KhaiBaoTrieuChung.objects.filter(patient=patient).values('pk').get()
  patient_tc = KhaiBaoTrieuChung.objects.filter(id=patient_tc_id['pk']).values().get()
  #region TC
  Note = patient_tc['Note']
  TC1 = patient_tc['TC1']
  TC2 = patient_tc['TC2']
  TC3 = patient_tc['TC3']
  TC4 = patient_tc['TC4']
  TC5 = patient_tc['TC5']
  TC6 = patient_tc['TC6']
  TC7 = patient_tc['TC7']
  TC8 = patient_tc['TC8']
  TC9 = patient_tc['TC9']
  TC10 = patient_tc['TC10']
  TC11 = patient_tc['TC11']
  TC12 = patient_tc['TC12']
  TC13 = patient_tc['TC13']
  TC14 = patient_tc['TC14']
  TC15 = patient_tc['TC15']
  TC16 = patient_tc['TC16']
  TC17 = patient_tc['TC17']
  TC18 = patient_tc['TC18']
  TC19 = patient_tc['TC19']
  TC20 = patient_tc['TC20']
  TC21 = patient_tc['TC21']
  TC22 = patient_tc['TC22']
  TC23 = patient_tc['TC23']
  #endregion

  #region name
  patient_id = Patient.objects.filter(id=patient_id).values('patientUser_id').get()
  patient_profile = Account.objects.filter(id=patient_id['patientUser_id']).values('user_id').get()
  first_name = User.objects.filter(id=patient_profile['user_id']).values('first_name').get()
  last_name = User.objects.filter(id=patient_profile['user_id']).values('last_name').get()
  name = first_name['first_name'] + " " + last_name['last_name']
  #endregion
  
  value_id = DanhGia.objects.filter(patient=patient).values('pk').get()
  
  value = DanhGia.objects.get(id=value_id["pk"])

  if request.method=='POST':
    value_patient = DanhGiaTrieuChung(request.POST, instance=value)
    if value_patient.is_valid():
      value_patient.save()
      messages.success(request, 'Cập nhật tình trạng bệnh nhân thành công!')
  else:
    value_patient = DanhGiaTrieuChung(instance=value)
  id = patient_id
  context = {
    'TC1': TC1,'TC2': TC2,'TC3': TC3,'TC4': TC4,'TC5': TC5,'TC6': TC6,'TC7': TC7,'TC8': TC8,
    'TC9': TC9,'TC10': TC10,'TC11': TC11,'TC12': TC12,'TC13': TC13,'TC14': TC14,'TC15': TC15,'TC16': TC16,
    'TC17': TC17,'TC18': TC18,'TC19': TC19,'TC20': TC20,'TC21': TC21,'TC22': TC22,'TC23': TC23,'Note':Note,
    'value_patient': value_patient,
    'name' : name,
    'patient_id':id
  }
  return render(request,'base/tc_value.html', context)                                                

@login_required(login_url="login")
def medical_update(request, patient_id):
  patient = Patient.objects.get(id=patient_id)
  medical_id = MedicalRecord.objects.filter(patient=patient).values('pk').get()
  medical = MedicalRecord.objects.get(id=medical_id["pk"])
  if request.method=='POST':
    form = MedicalRecordUpdate(request.POST, instance=medical)
    if form.is_valid():
      form.save()
      messages.success(request, 'Cập nhật tình trạng bệnh nhân thành công!')
  else:
    form = MedicalRecordUpdate(instance=medical)
  context = {'form':form}
  return render(request,'base/medical_update.html', context) 

@login_required(login_url="login")
def delete_patient_home(request, patient_id):
  instance = Patient.objects.get(id=patient_id)
  instance.delete()
  return redirect("patienthome")

@login_required(login_url="login")
def delete_patient_hospital(request, patient_id):
  instance = Patient.objects.get(id=patient_id)
  instance.delete()
  return redirect("patienthospital")

@login_required(login_url="login")
def delete_patient_ok(request, patient_id):
  instance = Patient.objects.get(id=patient_id)
  instance.delete()
  return redirect("patientok")