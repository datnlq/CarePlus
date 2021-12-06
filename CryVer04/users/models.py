from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class HealthDeclaration(models.Model):
  user = models.OneToOneField(User, related_name='healthdeclare', on_delete=models.CASCADE)
  CacNuocDiQua = models.CharField(max_length=200, default=" ",  null=True, blank=True)
  company = models.CharField(max_length=50, default=" ", verbose_name="Công ty làm việc", null=True, blank=True)
  part = models.CharField(max_length=50, default=" ", verbose_name="Bộ phận làm việc", null=True, blank=True)
  BHYT = models.BooleanField(verbose_name="Có thẻ bảo hiểm y tế", default=False)
  Sot = models.BooleanField(verbose_name="Sốt", default=False)
  Ho = models.BooleanField(verbose_name="Ho", default=False)
  KhoTho = models.BooleanField(verbose_name="Khó thở", default=False)
  ViemPhoi = models.BooleanField(verbose_name="Viêm phổi", default=False)
  DauHong = models.BooleanField(verbose_name="Đau họng", default=False)
  Metmoi = models.BooleanField(verbose_name="Mệt mỏi", default=False)
  NghiNgo = models.BooleanField(verbose_name="Người bệnh hoặc nghi ngờ, mắc bệnh COVID-19 (*)", default=False)
  CoBenh = models.BooleanField(verbose_name="Người từ nước có bệnh COVID-19 (*)", default=False)
  CoBieuHien = models.BooleanField(verbose_name="Người có biểu hiện (Sốt, ho, khó thở, Viêm phổi) (*)", default=False)
  Gan = models.BooleanField(verbose_name="Bệnh gan mãn tính (*)", default=False)
  Mau = models.BooleanField(verbose_name="Bệnh máu mãn tính (*)", default=False)
  Phoi = models.BooleanField(verbose_name="Bệnh phổi mãn tính (*)", default=False)
  Than = models.BooleanField(verbose_name="Bệnh thận mãn tính (*)", default=False)
  TimMach = models.BooleanField(verbose_name="Bệnh tim mạch (*)", default=False)
  HuyetApCao = models.BooleanField(verbose_name="Huyết áp cao (*)", default=False)
  SuyGiamMienDich = models.BooleanField(verbose_name="Suy giảm miễn dịch (*)", default=False)
  Ghep = models.BooleanField(verbose_name="Người nhận ghép tạng, Tủy xương (*)", default=False)
  TieuDuong = models.BooleanField(verbose_name="Tiểu đường (*)", default=False)
  UngThu = models.BooleanField(verbose_name="Ung thư (*)", default=False)
  ThaiKy = models.BooleanField(verbose_name="Bạn có đang trong thời gian thai kỳ hay không? (*)", default=False)

  def __str__(self):
    return '%s %s' % (self.user.first_name, self.user.last_name)

