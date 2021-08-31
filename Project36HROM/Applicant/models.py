from django.db import models


class RegistrationModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    dob = models.DateField()
    email = models.EmailField()
    gender = models.CharField(max_length=10)
    mobile = models.CharField(max_length=13)
    address = models.CharField(max_length=30)
    uname = models.CharField(max_length=30)
    password = models.CharField(max_length=20)


class ApplicationModel(models.Model):
    applicationid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    dob = models.DateField()
    email = models.EmailField(max_length=20)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField()
    address = models.TextField(max_length=30)
    qualification = models.CharField(max_length=20)
    post = models.CharField(max_length=30)
    percent = models.FloatField()
    resume = models.FileField(upload_to="resume/")

    def __str__(self):
        return str(self.applicationid)
