# Generated by Django 5.0.4 on 2024-05-01 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employ', '0002_employee_user_alter_employee_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='profile_images/'),
        ),
    ]