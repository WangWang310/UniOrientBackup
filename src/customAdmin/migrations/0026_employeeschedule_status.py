# Generated by Django 3.2.9 on 2022-11-23 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customAdmin', '0025_employeeschedule'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeschedule',
            name='status',
            field=models.CharField(blank=True, default='INACTIVE', max_length=150, null=True),
        ),
    ]
