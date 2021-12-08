from django.contrib import admin
from accounts.models import Account, Doctor,  Patient
from django.contrib.auth.models import User 
from django.contrib.auth.admin import UserAdmin

from users.models import HealthDeclaration
from doctor.models import MedicalRecord
from accounts.models import Patient
from patient.models import DanhGia, KhaiBaoTrieuChung

admin.site.register(Account)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(HealthDeclaration)
admin.site.register(MedicalRecord)
admin.site.register(KhaiBaoTrieuChung)
admin.site.register(DanhGia)