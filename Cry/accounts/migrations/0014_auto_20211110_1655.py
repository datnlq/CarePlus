# Generated by Django 3.2.8 on 2021-11-10 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_huyen'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiaChi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_tinh', models.CharField(blank=True, max_length=50, null=True)),
                ('ma_TP', models.CharField(blank=True, max_length=2, null=True)),
                ('ten_quanhuyen', models.CharField(blank=True, max_length=50, null=True)),
                ('ma_QH', models.CharField(blank=True, max_length=3, null=True)),
                ('ten_phuongxa', models.CharField(blank=True, max_length=50, null=True)),
                ('ma_PX', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Huyen',
        ),
        migrations.DeleteModel(
            name='Tinh',
        ),
    ]
