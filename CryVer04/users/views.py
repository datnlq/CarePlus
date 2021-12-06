from django.contrib.auth import authenticate, login, logout, get_user_model, models
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from accounts.models import Account, Doctor
from .forms import DoctorUpdateForm, HealthyDeclareUpdateForm, LoginForm, ProfileUpdateForm, RegisterForm, UserUpdateForm
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users import forms
from .models import HealthDeclaration
from django.contrib import messages

User = get_user_model()

def login_view(request):
  form = LoginForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get("username")
    password = form.cleaned_data.get("password")
    user = authenticate(request, username=username, password=password)
    if user != None:
      login(request, user)
      return redirect("home")
    else:
      #attempt = request.session.get("attempt") or 0
      #request.session['attempt'] = attempt + 1
      #return redirect("/invalid-password")
      request.session['invalid_user'] = 1 #1==True
  return render(request, 'users/login.html', {'form': form})

@login_required(login_url="login")
def logout_view(request):
  logout(request)
  return redirect("home")

def register(request):
  form = RegisterForm(request.POST or None)
  if form.is_valid():
    username = form.cleaned_data.get("username")
    email = form.cleaned_data.get("email")
    password = form.cleaned_data.get("password1")
    password2 = form.cleaned_data.get("password2")
    first_name = form.cleaned_data.get("first_name")
    last_name = form.cleaned_data.get("last_name")
    try:
      user = User.objects.create_user(username, email, password)
      user.first_name = first_name
      user.last_name = last_name
      user.save()
    except:
      user = None
    if user != None:
      login(request, user)
      return redirect("home")
    else:
      request.session['register_error'] = 1 #1==True
  return render(request, 'users/register.html', {'form': form})

@login_required(login_url="login")
def profile(request):
    return render(request,'users/profile.html')

@login_required(login_url="login")
def profile_update(request):
  doctor_id = Doctor.objects.filter(doctorUser=request.user.profile).values('pk').get()
  doctor = Doctor.objects.get(id=doctor_id['pk'])
  if request.method=='POST':
    user_form = UserUpdateForm(request.POST, instance=request.user)
    profile_form = ProfileUpdateForm(
      request.POST, request.FILES, instance=request.user.profile)
    doctor_form = DoctorUpdateForm(request.POST, instance=doctor)
    
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      if request.user.profile.type_account == "Bác sĩ":
        doctor_form.save()
      messages.success(request, 'Đã thay đổi thông tin thành công!')
      return redirect("profile-update")
  else:
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
    if request.user.profile.type_account == "Bác sĩ":
        doctor_form = DoctorUpdateForm(instance=doctor)
  context = {
    'user_form': user_form,
    'profile_form': profile_form,
    'doctor_form': doctor_form
  }
  return render(request,'users/profile_update.html', context)

@login_required(login_url="login")
def healthydeclare_update(request):
  user_id = HealthDeclaration.objects.filter(user=request.user).values('pk').get()
  healthform = HealthDeclaration.objects.get(id=user_id['pk'])
  if request.method=='POST':
    form = HealthyDeclareUpdateForm(request.POST, instance=healthform)
    if form.is_valid():
      form.save()
      messages.success(request, 'Đã thay đổi khai báo y tế của bạn!')
      return redirect("healthdeclare-update")
  else:
    form = HealthyDeclareUpdateForm(instance=healthform)
  context = {
    'form': form,
  }
  return render(request,'users/healthdeclare_update.html', context)