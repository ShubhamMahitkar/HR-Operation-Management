# Generated by Django 3.0 on 2020-04-15 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationModel',
            fields=[
                ('applicationid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('dob', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=20)),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.IntegerField()),
                ('address', models.TextField(max_length=60)),
                ('qualification', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=30)),
                ('percent', models.FloatField()),
                ('resume', models.FileField(upload_to='resume/')),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=10)),
                ('mobile', models.CharField(max_length=13)),
                ('address', models.CharField(max_length=60)),
                ('uname', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]