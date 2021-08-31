from django import forms
from Manager.models import NewRecruitModel
from Manager.models import NewInterViewSchModel


class DateInput(forms.DateInput):
    input_type = 'date'

class NewRecruitForm(forms.ModelForm):
    class Meta:
        model = NewRecruitModel
        fields = "__all__"
        widgets = {"regstart": DateInput, "lastdate": DateInput}



class NewInterviewSchForm(forms.ModelForm):
    class Meta:
        model = NewInterViewSchModel
        fields ="__all__"
        widgets = {"sch_date": DateInput}
