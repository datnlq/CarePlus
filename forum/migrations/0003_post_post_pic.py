# Generated by Django 3.2.8 on 2021-12-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_topic_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_pic',
            field=models.ImageField(blank=True, default='', null=True, upload_to='', verbose_name='post'),
        ),
    ]
