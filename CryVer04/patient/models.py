from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey
from django.db.models.signals import post_save
from accounts.models import Patient

# Create your models here.
class KhaiBaoTrieuChung(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  TC1 = models.BooleanField(verbose_name=u"Các triệu chứng thường gặp (khởi phát) nặng lên liên tục không đỡ", null=True, blank=True)
  TC2 = models.BooleanField(verbose_name=u"Sốt cao từ 39 độ C không đáp ứng với thuốc hạ sốt (sốt trở lại trong vòng 02h sau dùng thuốc)", null=True, blank=True)
  TC3 = models.BooleanField(verbose_name=u"Khó thở không thể làm việc được phải nghỉ ngơi", null=True, blank=True)
  TC4 = models.BooleanField(verbose_name=u"Mệt mỏi, sinh hoạt khó khăn", null=True, blank=True)
  TC5 = models.BooleanField(verbose_name=u"Huyết áp tăng cao từ 160/100 mmHG không đáp ứng với thuốc thường dùng", null=True, blank=True)
  TC6 = models.BooleanField(verbose_name=u"Đo huyết áp 2 lần có giá trị trung bình dưới 85/5mmHG", null=True, blank=True)
  TC7 = models.BooleanField(verbose_name=u"Nhịp tim tăng cao trên 120 lần/phút hoặc xuống dưới 50 lần/phút, hoặc nhịp thở từ 25 lần/phút", null=True, blank=True)
  TC8 = models.BooleanField(verbose_name=u"Khó thở nhiều không thể nằm để thở", null=True, blank=True)
  TC9 = models.BooleanField(verbose_name=u"Đau tức ngực thành cơn kéo dài từ 5'", null=True, blank=True)
  TC10 = models.BooleanField(verbose_name=u"Mất khả năng nói hoặc cử động", null=True, blank=True)
  TC11 = models.BooleanField(verbose_name=u"Lơ mơ, không tỉnh táo", null=True, blank=True)
  TC12 = models.BooleanField(verbose_name=u"SpO2 < 94% khi nghỉ hoặc tụt SpO2 xuống < 94% sau gắng sức (nếu có thiết bị đo SpO2 tại nhà", null=True, blank=True)
  TC13 = models.BooleanField(verbose_name=u"Tiêu chảy", null=True, blank=True)
  TC14 = models.BooleanField(verbose_name=u"Viêm kết mạc", null=True, blank=True)
  TC15 = models.BooleanField(verbose_name=u"Mất vị giác hoặc khứu giác", null=True, blank=True)
  TC16 = models.BooleanField(verbose_name=u"Da nổi mẩn hay ngón tay hoặc ngón chân bị tất đỏ hoặc tím tái", null=True, blank=True)
  TC17 = models.BooleanField(verbose_name=u"Sốt dưới 39 độ C", null=True, blank=True)
  TC18 = models.BooleanField(verbose_name=u"Ho khan, đau họng", null=True, blank=True)
  TC19 = models.BooleanField(verbose_name=u"Mệt mỏi nhưng vẫn sinh hoạt bình thường", null=True, blank=True)
  TC20 = models.BooleanField(verbose_name=u"Đau nhức cơ thể", null=True, blank=True)
  TC21 = models.BooleanField(verbose_name=u"Khó thở nhẹ", null=True, blank=True)
  TC22 = models.BooleanField(verbose_name=u"Đau đầu", null=True, blank=True)
  TC23 = models.BooleanField(verbose_name=u"Xác nhận không có triệu chứng gì trong các triệu chứng kệ trên", null=True, blank=True)
  Note = models.TextField(verbose_name=u"Ghi chú", max_length=500, null=True, blank=True)

  def __str__(self):
      return '%s %s' % (self.patient.patientUser.user.first_name, self.patient.patientUser.user.last_name)

class DanhGia(models.Model):
  patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
  DanhGia = models.CharField(
    max_length=23,
    default='Xanh',
    verbose_name=u"Đánh giá: ",
    choices=[('Xanh', 'Xanh'),
            ('Vàng', 'Vàng',),
            ('Đỏ', 'Đỏ',),
          ],
    null=True, blank=True
  )

  def __str__(self):
      return '%s %s' % (self.patient.patientUser.user.first_name, self.patient.patientUser.user.last_name)

def create_tc(sender, instance, created, **kwards):
  if created:
     KhaiBaoTrieuChung.objects.create(patient=instance)
post_save.connect(create_tc, sender=Patient)

def create_tc(sender, instance, created, **kwards):
  if created:
    DanhGia.objects.create(patient=instance)
post_save.connect(create_tc, sender=Patient)