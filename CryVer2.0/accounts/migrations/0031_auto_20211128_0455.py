# Generated by Django 3.2.8 on 2021-11-27 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0030_rename_medicalrecorduser_medicalrecord_record'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctorUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='accounts.account'),
        ),
        migrations.AlterField(
            model_name='medicalrecord',
            name='record',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='record', to=settings.AUTH_USER_MODEL),
        ),
    ]