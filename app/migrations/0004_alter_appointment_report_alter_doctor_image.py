# Generated by Django 5.0.6 on 2024-05-24 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_doctor_image_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='report',
            field=models.FileField(upload_to='patient'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='image',
            field=models.FileField(upload_to='doctor'),
        ),
    ]
