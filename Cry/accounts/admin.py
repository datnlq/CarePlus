from django.contrib import admin
from accounts.models import Account, Assistant, Doctor
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin

admin.site.register(Account)
admin.site.register(Doctor)
admin.site.register(Assistant)









