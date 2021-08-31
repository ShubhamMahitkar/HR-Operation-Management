from django.db import models
from Applicant.models import ApplicationModel
from Interviewer.models import NewInterviewModel

# class ShortlistedModel(models.Model):
#     applicationid = models.ForeignKey(ApplicationModel, on_delete=models.CASCADE)
#     applicationname = models.ForeignKey(ApplicationModel, on_delete=models.CASCADE)
#     edu = models.ForeignKey(ApplicationModel, on_delete=models.CASCADE)
#     dob = models.ForeignKey(ApplicationModel, on_delete=models.CASCADE)
#     point = models.ForeignKey(ApplicationModel, on_delete=models.CASCADE)
#     email = models.ForeignKey(ApplicationModel, on_delete=models.CASCADE)
#     contact = models.ForeignKey(ApplicationModel, on_delete=models.CASCADE)
#     result = models.ForeignKey(NewInterviewModel, on_delete=models.CASCADE)

#
# class Selected(models.Model):
#     interviewid =
#     interviewer =
#     applicationid =
#     scheduletime =
#     result =
#
#
# class Rejected(models.Model):
#     interviewid =
#     interviewer =
#     applicationid =
#     scheduletime =
#     result =
