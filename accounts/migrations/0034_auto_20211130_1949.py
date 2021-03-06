# Generated by Django 3.2.8 on 2021-11-30 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0033_rename_doctoruser_patient_patientuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.AddField(
            model_name='patient',
            name='doctorUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.doctor'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patientUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='accounts.account'),
        ),
    ]
