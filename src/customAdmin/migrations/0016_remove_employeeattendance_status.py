# Generated by Django 3.2.9 on 2022-11-03 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0015_employeeattendance_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeeattendance',
            name='status',
        ),
    ]