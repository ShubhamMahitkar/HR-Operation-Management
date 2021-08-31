from django.db import models

from Admin.models import AdminModel
from Applicant.models import ApplicationModel


class NewRecruitModel(models.Model):
    opcode = models.IntegerField(primary_key=True, unique=True)
    quali = models.CharField(max_length=30)
    regstart = models.DateField()
    agelim = models.IntegerField()
    lastdate = models.DateField()
    deptid = models.CharField(max_length=10)
    nofposn = models.IntegerField()
    desc = models.CharField(max_length=100)
    resp = models.CharField(max_length=250)
    cont = models.IntegerField()

    def __str__(self):
        return self.opcode

class NewInterViewSchModel(models.Model):
    application_id = models.ForeignKey(ApplicationModel, on_delete=models.CASCADE)
    emp_id = models.OneToOneField(AdminModel, on_delete=models.CASCADE)
    sch_date = models.DateField()

    def __str__(self):
        return str(self.sch_date)

