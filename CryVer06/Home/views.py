from django.shortcuts import render
from accounts.models import Account

# Create your views here.
def home_view(request):
  return render(request,'base/index.html')
