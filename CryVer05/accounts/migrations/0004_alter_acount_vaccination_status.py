# Generated by Django 3.2.8 on 2021-11-10 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_acount_vaccination_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acount',
            name='vaccination_status',
            field=models.CharField(choices=[('1', '1 mũi'), ('2', '2 mũi'), ('0', 'Chưa tiêm')], max_length=10),
        ),
    ]
