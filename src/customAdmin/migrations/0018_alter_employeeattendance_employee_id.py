# Generated by Django 3.2.6 on 2021-11-30 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0017_alter_employeeattendance_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeattendance',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customAdmin.employee'),
        ),
    ]