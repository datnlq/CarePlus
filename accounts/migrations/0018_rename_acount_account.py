# Generated by Django 3.2.8 on 2021-11-10 18:37

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0017_auto_20211111_0114'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Acount',
            new_name='Account',
        ),
    ]
