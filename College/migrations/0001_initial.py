# Generated by Django 3.0.5 on 2021-04-03 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('roll_no', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('student_name', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty_name', models.CharField(max_length=50, unique=True)),
                ('subject', models.CharField(max_length=30)),
            ],
        ),
    ]
