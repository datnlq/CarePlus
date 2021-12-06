from django.contrib.auth import get_user_model
from django import forms

from accounts.models import Account
from .models import HealthDeclaration

User = get_user_model()

class RegisterForm(forms.Form):
  username = forms.CharField(label="Tên đăng nhập", widget=forms.TextInput(attrs={'class':'form-control'}))
  first_name = forms.CharField(label="Họ", widget=forms.TextInput(attrs={'class':'form-control'}))
  last_name = forms.CharField(label="Tên", widget=forms.TextInput(attrs={'class':'form-control'}))
  
  email = forms.EmailField(label="Email", widget=forms.TextInput(attrs={'class':'form-control'}))
  password1 = forms.CharField(
    label="Mật khẩu",
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "id": "user-password"
      }
    )
  )
  password2 = forms.CharField(
    label="Xác nhận mật khẩu",
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "id": "user-confirm-password"
      }
    )
  )


  def clean_username(self):
    username = self.cleaned_data.get("username")
    qs = User.objects.filter(username__iexact=username)
    if qs.exists():
      raise forms.ValidationError("This is an invalid user, please pick another.")
    return username

  def clean_email(self):
    email = self.cleaned_data.get("email")
    qs = User.objects.filter(username__iexact=email)
    if qs.exists():
      raise forms.ValidationError("This email is already in use.")
    return email
    
class LoginForm(forms.Form):
  username = forms.CharField(label="Tên đăng nhập", widget=forms.TextInput(attrs={'class':'form-control'}))
  password = forms.CharField(
    label="Mật khẩu",
    widget=forms.PasswordInput(
      attrs={
        "class": "form-control",
        "id": "user-password"
      }
    )
  )

  #def clean(self):
    #username=self.cleaned_data.get("username")
    #password=self.cleaned_data.get("password") """

  def clean_username(self):
    username = self.cleaned_data.get("username")
    qs = User.objects.filter(username__iexact=username)
    if not qs.exists():
      raise forms.ValidationError("Tên đăng nhập hoặc mật khẩu không hợp lệ")
    return username

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name', 
            'last_name', 
            'email', 
        ]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'CMND',
            'birthday',
            'gender',
            'city',
            'district',
            'commune',
            'address',
            'phone',
            'career',
            'vaccination_status',
            'type_account'
        ]

class UserUpdateForm(forms.ModelForm):
    class Meta:
      model = User
      fields = [ 
        'first_name', 
        'last_name', 
        'email', 
      ]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = [
            'CMND',
            'birthday',
            'gender',
            'city',
            'district',
            'commune',
            'address',
            'phone',
            'career',
            'profile_pic',
            'vaccination_status',
        ]

