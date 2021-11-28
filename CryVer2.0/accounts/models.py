from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Account(models.Model):
  user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
  birthday = models.DateField(verbose_name=u"Ngày sinh", null=True, blank=True)
  gender = models.CharField(
    max_length=6,
    default='',
    verbose_name=u"Giới tính",
    choices=[('Nam', 'Nam'),('Nữ', 'Nữ')]
  )
  city = models.CharField(verbose_name=u"Tỉnh, thành phố", default="", max_length=50, null=True, blank=True)
  district = models.CharField(verbose_name=u"Quận, huyện", default="", max_length=50, null=True, blank=True)
  commune = models.CharField(verbose_name=u"Xã, phường", default="", max_length=50, null=True, blank=True)
  address = models.CharField(verbose_name=u"Địa chỉ", default="", max_length=200, null=True, blank=True)
  phone = models.CharField(verbose_name=u"Số điện thoại", default="", max_length=50, null=True, blank=True)
  career = models.CharField(verbose_name=u"Nghề nghiệp", default="", max_length=50, null=True, blank=True)
  profile_pic = models.ImageField(verbose_name=u"Ảnh đại diện", default="card.svg", null=True, blank=True)
  vaccination_status = models.CharField(
    max_length=10, 
    default='2 mũi',
    choices=[('1', '1 mũi'),('2', '2 mũi'),('0', 'Chưa tiêm')]
  )
  type_account = models.CharField(
    max_length=10, 
    default='Khác',
    choices=[('BS', 'Bác sĩ'),('BN', 'Bệnh nhân'),('HT', 'Hỗ trợ'),('K', 'Khác')]
  )

  def __str__(self):
    return '%s %s' % (self.user.first_name, self.user.last_name)
  
  def isDoctor(self):
    if self.type_account=="Bác sĩ":
      return True
    else:
      return False
 
class Doctor(models.Model):
    doctorUser = models.OneToOneField(Account, related_name='doctor', on_delete=models.CASCADE)
    ChuyenKhoa = models.CharField(max_length=50, default='Chuyên khoa')
    BenhVien = models.CharField(max_length=50, default='Bệnh viện', blank=True)

    def __str__(self):
      return '%s %s' % (self.doctorUser.user.first_name, self.doctorUser.user.last_name)

class Assistant(models.Model):
    assistantUser = models.OneToOneField(Account, on_delete=models.CASCADE)
    doctorUser = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    
    def __str__(self):
      return '%s %s' % (self.assistantUser.user.first_name, self.assistantUser.user.last_name)

class MedicalRecord(models.Model):
    user = models.OneToOneField(User, related_name='record',  on_delete=models.CASCADE)
    doctorUser = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    cccd = models.CharField(max_length=50, default='CCCD/CMND')
    bhyt = models.CharField(max_length=50, default='BHYT')
    ques1 = models.BooleanField (verbose_name="Trong vong 14 ngay qua", default=False)
    ques2 = models.BooleanField (verbose_name="Trong vong 14 ngay qua", default=False)
    ques3 = models.BooleanField (verbose_name="Trong vong 14 ngay qua", default=False)
    ques4 = models.BooleanField (verbose_name="Trong vong 14 ngay qua", default=False)
    ques5 = models.BooleanField (verbose_name="Trong vong 14 ngay qua", default=False)

    date = models.DateField(verbose_name=u"Ngày khám", null=True, blank=True)
    disease = models.CharField(verbose_name=u"Bệnh", default="", max_length=50, null=True, blank=True)
    treatment = models.CharField(verbose_name=u"Điều trị", default="", max_length=50, null=True, blank=True)
    note = models.CharField(verbose_name=u"Ghi chú", default="", max_length=200, null=True, blank=True)
    status = models.CharField(
      max_length=20, 
      default='Đang điều trị',
      choices=[('Đang điều trị', 'Đang điều trị'),('Đã điều trị', 'Đã điều trị')]
    )  
    def __str__(self):
      return '%s %s' % (self.user.first_name, self.user.last_name)

    


