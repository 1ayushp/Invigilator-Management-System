# Generated by Django 4.0.6 on 2022-11-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_addbuilding_profile_addexam_profile_addroom_profile_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='testing',
            name='newappname',
            field=models.CharField(default='', max_length=122),
        ),
        migrations.AddField(
            model_name='testing',
            name='newappphone',
            field=models.CharField(default='', max_length=12),
        ),
    ]
