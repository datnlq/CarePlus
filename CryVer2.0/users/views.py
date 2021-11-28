from django.contrib.auth import authenticate, login, logout, get_user_model, models
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from accounts.models import Account
from .forms import * 
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users import forms


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
  if request.method=='POST':
    user_form = UserUpdateForm(request.POST, instance=request.user)
    profile_form = ProfileUpdateForm(
      request.POST, request.FILES, instance=request.user.profile)
    if user_form.is_valid() and profile_form.is_valid():
      user_form.save()
      profile_form.save()
      return redirect("profile")
  else:
    user_form = UserUpdateForm(instance=request.user)
    profile_form = ProfileUpdateForm(instance=request.user.profile)
  context = {
    'user_form': user_form,
    'profile_form': profile_form,
  }
  return render(request,'users/profile_update.html', context)
  

@login_required(login_url="login")
def medical_record(request):
  user = UserForm(instance=request.user)
  record = MedicalRecordForm(instance=request.user.record)
  context = {
    'user': user,
    'record': record,
  }
  return render(request,'users/medical_record.html',context)


@login_required(login_url="login")
def medical_record_update(request):
  if request.method=='POST':
    record_form = RecordUpdateForm(request.POST, instance=request.user.record)
    if record_form.is_valid():
      record_form.save()
      return redirect("medical-record")    
  else:
    record_form = RecordUpdateForm(instance=request.user.record)
    
  context = {
      'record_form': record_form,
    }
  return render(request,'users/record_update.html', context)

