# Generated by Django 3.2.6 on 2022-10-12 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0012_alter_employee_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='passExp',
            field=models.DateField(blank=True, null=True),
        ),
    ]
