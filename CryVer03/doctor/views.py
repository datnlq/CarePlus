from django.contrib.auth import get_user_model
from accounts.models import Account, Doctor, Patient
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render

from doctor.forms import AddPatient

User = get_user_model()

class PatientHome(LoginRequiredMixin,ListView):
  model = Patient
  context_object_name = 'patients1'
  template_name = 'base/patient_home.html'

  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    profile = Account.objects.get(user__exact=self.request.user)
    doctor = Doctor.objects.get(doctorUser__exact=profile)
    context['patients1'] = context['patients1'].filter(doctorUser=doctor)
    context['patients_home'] = context['patients1'].filter(doctorUser=doctor).filter(TinhTrang="Đang điều trị tại nhà")
    context['count_home'] = context['patients1'].filter(TinhTrang="Đang điều trị tại nhà").count()
    return context

class PatientHospital(LoginRequiredMixin,ListView):
  model = Patient
  context_object_name = 'patients2'
  template_name = 'base/patient_hospital.html'

  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    profile = Account.objects.get(user__exact=self.request.user)
    doctor = Doctor.objects.get(doctorUser__exact=profile)
    context['patients2'] = context['patients2'].filter(doctorUser=doctor)
    context['patients_hospital'] = context['patients2'].filter(doctorUser=doctor).filter(TinhTrang="Đã nhập viện")
    context['count_hospital'] = context['patients2'].filter(TinhTrang="Đã nhập viện").count()
    return context

class PatientOK(LoginRequiredMixin,ListView):
  model = Patient
  context_object_name = 'patients3'
  template_name = 'base/patient_ok.html'

  def get_context_data(self, **kwargs): 
    context = super().get_context_data(**kwargs)
    profile = Account.objects.get(user__exact=self.request.user)
    doctor = Doctor.objects.get(doctorUser__exact=profile)
    context['patients3'] = context['patients3'].filter(doctorUser=doctor)
    context['patients_ok'] = context['patients3'].filter(doctorUser=doctor).filter(TinhTrang="Đã khỏi bệnh")
    context['count_ok'] = context['patients3'].filter(TinhTrang="Đã khỏi bệnh").count()
    return context

def add_patient(request):
  form = AddPatient(request.POST or None)
  if form.is_valid():
    CMND = form.cleaned_data.get("CMND") 
    try:
      patientUser = Account.objects.filter(CMND=CMND)
      doctorUser = Account.objects.filter(user=request.user)
      patient = Patient.create(patientUser=patientUser, doctorUser=doctorUser)
      print(patient)
      patient.save()
    except:
      user = None
    if user != None:
      return redirect("")
    else:
      request.session['patient_error'] = 1 #1==True
  return render(request, 'users/register.html', {'form': form})
