# Generated by Django 3.2.8 on 2021-11-25 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_auto_20211125_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='type_account',
            field=models.CharField(choices=[('BS', 'Bác sĩ'), ('BN', 'Bệnh nhân'), ('HT', 'Hỗ trợ'), ('K', 'Khác')], default='Khác', max_length=10),
        ),
    ]