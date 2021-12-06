from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save

# Create your models here.
class Account(models.Model):
  user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
  CMND = models.CharField(verbose_name=u"CMND/CCCD", default="Chưa có", max_length=50, null=True, blank=True)
  birthday = models.DateField(verbose_name=u"Ngày sinh", null=True, blank=True)
  gender = models.CharField(
    max_length=6,
    default='Nữ',
    verbose_name=u"Giới tính",
    choices=[('Nam', 'Nam'),('Nữ', 'Nữ')]
  )
  city = models.CharField(verbose_name=u"Tỉnh, thành phố", default="Hà Nội", max_length=50, null=True, blank=True)
  district = models.CharField(verbose_name=u"Quận, huyện", default="Huyện Bắc Bình", max_length=50, null=True, blank=True)
  commune = models.CharField(verbose_name=u"Xã, phường", default="Xã Bình An", max_length=50, null=True, blank=True)
  address = models.CharField(verbose_name=u"Địa chỉ", default="256 Thôn An Hoà", max_length=200, null=True, blank=True)
  phone = models.CharField(verbose_name=u"Số điện thoại", default="0123456789", max_length=50, null=True, blank=True)
  career = models.CharField(verbose_name=u"Nghề nghiệp", default="Sinh viên", max_length=50, null=True, blank=True)
  profile_pic = models.ImageField(verbose_name=u"Ảnh đại diện", default="card.svg", null=True, blank=True)
  vaccination_status = models.CharField(
    max_length=10, 
    default='2 mũi',
    choices=[('1', '1 mũi'),('2', '2 mũi'),('0', 'Chưa tiêm')]
  )
  type_account = models.CharField(
    max_length=10, 
    default='Khác',
    choices=[('Bác sĩ', 'Bác sĩ'),('Bệnh nhân', 'Bệnh nhân'),('Khác', 'Khác')]
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

class Patient(models.Model):
  patientUser = models.OneToOneField(Account, related_name='patient', on_delete=models.CASCADE)
  doctorUser = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
  NgayPhatBenh = models.DateField(verbose_name=u"Ngày phát bệnh", null=True, blank=True)
  LyDo = models.CharField(verbose_name=u"Lý do nhiễm bệnh", max_length=200)
  SDTNguoiThan = models.CharField(verbose_name=u"Số điện thoại người thân", max_length=10)
  BenhNen = models.CharField(verbose_name=u"Bệnh nền", max_length=200)
  NoiDiQua = models.CharField(verbose_name=u"Nơi đã đi qua", max_length=300)
  TinhTrang = models.CharField(
    max_length=23,
    default='Đang điều trị tại nhà',
    verbose_name=u"Tình trạng",
    choices=[('Đang điều trị tại nhà', 'Đang điều trị tại nhà'),
            ('Đã nhập viện', 'Đã nhập viện',),
            ('Đã khỏi bệnh', 'Đã khỏi bệnh',),
            ('Đã tử vong', 'Đã tử vong',)
          ]
  )

  @classmethod
  def create(cls, patientUser, doctorUser):
    new_patient = cls(patientUser=patientUser, doctorUser=doctorUser)
    return new_patient
  def __str__(self):
      return '%s %s' % (self.patientUser.user.first_name, self.patientUser.user.last_name)


