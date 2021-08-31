from django.db import models

class AdminModel(models.Model):
    id = models.AutoField(primary_key=True)
    empname = models.CharField(max_length = 10)
    password = models.CharField(max_length = 8)
    designation = models.CharField(max_length = 10)
    address = models.CharField(max_length = 10)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return str(self.id)