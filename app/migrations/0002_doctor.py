# Generated by Django 5.0.6 on 2024-05-20 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('mobile_no', models.IntegerField()),
                ('gender', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('address', models.CharField(max_length=200)),
                ('degree', models.CharField(max_length=200)),
                ('experience', models.CharField(max_length=200)),
                ('Specialization', models.CharField(max_length=200)),
                ('image', models.FileField(upload_to='')),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
