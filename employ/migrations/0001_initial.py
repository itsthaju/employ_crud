# Generated by Django 5.0.4 on 2024-05-01 10:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('employee_code', models.CharField(max_length=20, unique=True)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=15)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employ.department')),
            ],
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='employ.employee')),
            ],
        ),
    ]
