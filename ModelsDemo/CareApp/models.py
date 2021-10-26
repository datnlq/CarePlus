from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import BooleanField

#region Profile 
class Profile(models.Model):
    SEX = [
        ('M', 'Male'), 
        ('F', 'Female')
    ]
    VACXIN_STATUS = [
        ('1', 'One dose'),
        ('2', 'Two dose'),
        ('0', 'Not yet')
    ]
    TYPE_USER = [
        ('DT', 'Doctor'),
        ('PT', 'Patient'),
        ('AS', 'Assistant'),
        ('OU', 'Other users')
    ]
    fullname = models.CharField(max_length=50, null=True, blank=True)
    sex = models.CharField(max_length=1, default='F', choices=SEX)
    birthday = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    career = models.CharField(max_length=50, null=True, blank=True)
    vaccination_status = models.CharField(max_length=2, default='0', choices=VACXIN_STATUS)

    class Meta:
        abstract = True
        ordering = ['fullname']

class Doctor(Profile):
    doctorUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    specialist = models.CharField(max_length=50, default='specialist')
    hospital = models.CharField(max_length=50, default='specialist', blank=True)

    class Meta(Profile.Meta):
        pass

class Patient(Profile):
    patientUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    diagnosisDate = models.DateTimeField(null=True, blank=True)
    relativePhoneNum = models.CharField(max_length=10, null=True, blank=True)
    doctorUser = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)

    class Meta(Profile.Meta):
        pass

class Assistant(Profile):
    assistantUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    doctorUser = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)

    class Meta(Profile.Meta):
        pass

class Others(Profile):
    otherUser = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta(Profile.Meta):
        pass
#endregion

#region MedicalRecord
class Medicine(models.Model):
    medicineName = models.CharField(max_length=50, blank=True, null=True, unique=True)
    producer = models.CharField(max_length=50, null=True, blank=True)
    distributor = models.CharField(max_length=50, null=True, blank=True)
    nation = models.CharField(max_length=50, null=True, blank=True)
    decription = models.CharField(max_length=50, null=True, blank=True)

class MedicalRecord(models.Model):
    recordID = models.CharField(max_length=50, blank=True, null=True, unique=True)
    doctorUser = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    patientUser = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
    prescriptionDate = models.DateTimeField(auto_now_add=True)
    time = models.IntegerField()
    note = models.TextField(null=True, blank = True)
    
class MRDetail(models.Model):
    recordID = models.ForeignKey(MedicalRecord, on_delete=models.CASCADE, blank=True)
    medicineName = models.ManyToManyField(Medicine)
    totalQuantity = models.IntegerField()
    morning = models.IntegerField(null=True)
    evening = models.IntegerField(null=True)
    night = models.IntegerField(null=True)
    note = models.TextField(null=True, blank = True)
#endregion

#region SymptomDeclaration
class Symptom(models.Model):
    nameSymptom = models.CharField(default='symptom', max_length=50, null=True, blank=True, unique=True)

class SymptomDeclaration(models.Model):
    STATUS = [
        ('B', 'Blue'),
        ('Y', 'Yellow'),
        ('R', 'Red')
    ]
    recordID = models.CharField(max_length=50, null=True, blank=True, unique=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, blank=True)
    timeModified = models.DateTimeField(auto_now_add=True)
    statePredict =  models.CharField(max_length=1, default = 'B', choices=STATUS)

class SDDetail(models.Model):
    recordID = models.ForeignKey(SymptomDeclaration, on_delete=models.CASCADE, default='symptom', blank=True)
    nameSymptom = models.ManyToManyField(Symptom)
    level = BooleanField(default=False)
#endregion

#region HealthDeclaration
class Information(models.Model):
    nameInfo = models.CharField(max_length=50, blank=True, null=True)
    group = models.CharField(max_length=50, blank=True, null=True)

class HealthDeclaration(models.Model):
    recordID = models.CharField(max_length=50, blank=True, null=True)
    #user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    DateModified = models.DateTimeField(auto_now_add=True)

class HDDetail(models.Model):
    recordID = models.ForeignKey(HealthDeclaration, on_delete=models.CASCADE)
    nameInfo = models.ManyToManyField(Information)
    state = BooleanField(default=False)
#endregion