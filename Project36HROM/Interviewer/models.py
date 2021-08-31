from django.db import models
from Manager.models import NewInterViewSchModel
from Applicant.models import ApplicationModel

class NewInterviewModel(models.Model):
    interviewid = models.IntegerField()
    interviewer = models.IntegerField()
    applicationid = models.IntegerField()
    schedule = models.OneToOneField(NewInterViewSchModel, on_delete=models.CASCADE)
    result = models.CharField(max_length=30)

