# Generated by Django 3.2.6 on 2022-10-12 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0013_alter_employee_passexp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='primaryemergencycontacts',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]