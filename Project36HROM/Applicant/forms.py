from Applicant.models import RegistrationModel
from Applicant.models import ApplicationModel
from django import forms


class RegistrationForm(forms.ModelForm):
    gen = (
        ('MALE', 'male'),
           ('FEMALE', 'female'),
           )
    gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)

    class Meta:
        model = RegistrationModel
        fields = '__all__'


class DateInput(forms.DateInput):
    input_type = 'date'


class ApplicationForm(forms.ModelForm):
    gen = (('MALE', 'male'), ('FEMALE', 'female'))
    gender = forms.ChoiceField(choices=gen, widget=forms.RadioSelect)
    dob = forms.CharField(widget=forms.DateInput)

    class Meta:
        model = ApplicationModel
        fields = '__all__'
        widgets = {"dob": DateInput}


