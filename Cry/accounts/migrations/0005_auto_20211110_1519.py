# Generated by Django 3.2.8 on 2021-11-10 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_acount_vaccination_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='acount',
            name='type_account',
            field=models.CharField(choices=[('BS', 'Bác sĩ'), ('BN', 'Bệnh nhân'), ('K', 'Khác')], default='Bác sĩ', max_length=10),
        ),
        migrations.AlterField(
            model_name='acount',
            name='gender',
            field=models.CharField(choices=[('Nam', 'Nam'), ('Nu', 'Nu')], max_length=6),
        ),
    ]
