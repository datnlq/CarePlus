# Generated by Django 3.2.8 on 2021-11-10 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20211110_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='xa',
            name='huyen',
        ),
        migrations.RemoveField(
            model_name='xa',
            name='tinh',
        ),
        migrations.AlterModelOptions(
            name='tinh',
            options={},
        ),
        migrations.AlterField(
            model_name='tinh',
            name='ten_tinh',
            field=models.CharField(blank=True, default='Tên tỉnh', max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Huyen',
        ),
        migrations.DeleteModel(
            name='Xa',
        ),
    ]
