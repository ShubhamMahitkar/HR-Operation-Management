from django import forms
from Interviewer.models import NewInterviewModel


class DateInput(forms.DateInput):
    input_type = 'date'


class NewInterviewForm(forms.ModelForm):
    class Meta:
        model = NewInterviewModel
        fields = "__all__"


