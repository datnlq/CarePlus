# Generated by Django 3.2.8 on 2021-11-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_delete_tinh'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tinh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_tinh', models.CharField(blank=True, default='Tên tỉnh', max_length=50, null=True)),
            ],
        ),
    ]
