# Generated by Django 4.0.6 on 2023-03-15 12:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_addexam_newaddexamcentre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addexam',
            name='newaddexamcentre',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='home.addexamcentre'),
            preserve_default=False,
        ),
    ]
