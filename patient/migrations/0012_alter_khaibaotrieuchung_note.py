# Generated by Django 3.2.8 on 2021-12-06 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0011_auto_20211207_0221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='khaibaotrieuchung',
            name='Note',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='Ghi chú'),
        ),
    ]
