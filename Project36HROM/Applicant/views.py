from django.shortcuts import render,redirect
from django.views.generic.base import View

from Applicant.function import handle_uploaded_file
from Applicant.models import RegistrationModel, ApplicationModel
from Applicant.forms import RegistrationForm, ApplicationForm


class ApplicationLogin(View):
    def get(self, request):
        request.session['status'] = True
        return render(request, 'applicant/applicant_home_page.html')

    def post(self, request):
        unm = request.POST['username']
        pas = request.POST['password']
        try:
            RegistrationModel.objects.get(uname=unm, password=pas)
            request.session['status'] = True
            return redirect('apply')

        except RegistrationModel.DoesNotExist:
            return redirect('applicant-login')


class ShowForm(View):
    def get(self, request):
        request.session['status'] = True
        return render(request, "applicant/applicant_register.html", {"form": RegistrationForm()})

    def post(self, request):
        if request.method == 'POST':
            request.session['status'] = True
            rf = RegistrationForm(request.POST)
            if rf.is_valid():
                rf.save()
                return redirect('applicant-login')
            else:
                rf = RegistrationForm()
                return render(request, 'applicant/applicant_register.html', {"form": rf})


class Apply(View):
    def get(self, request):
        return render(request, 'applicant/application_form.html', {"form": ApplicationForm()})

    def post(self, request):
        af = ApplicationForm(request.POST, request.FILES)
        if af.is_valid():
            handle_uploaded_file(request.FILES['resume'])
            af.save()
            return redirect('applicant-login')
        else:
            print("not uploaded in db")
            return render(request, "applicant/application_form.html", {"message": "Invalid data "})

