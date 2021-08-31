from django.contrib import messages
from django.shortcuts import render, redirect
from Applicant.models import ApplicationModel
from Interviewer.models import NewInterviewModel

def shortlisted(request):
    x = ApplicationModel.objects.all()
    return render(request, 'hrhead/shortlisted.html', {"data": x})


def selected(request):
    x = NewInterviewModel.objects.filter(result='Selected')
    return render(request, 'hrhead/selected.html', {"data": x})


def rejected(request):
    x = NewInterviewModel.objects.filter(result='Rejected')
    return render(request, 'hrhead/rejected.html', {"data": x})


def hr_logincheck(request):
    unm = request.POST['username']
    pas = request.POST['pass']
    if unm == 'hrhead' and pas == 'hrhead':
        request.session['status'] = True
        return render(request, 'hrhead/hrhead_home_page.html')
    else:
        messages.error(request,"Invalid username or password")
        return redirect('hr_login')


def logout(request):
    del request.session['status']
    return redirect('home')
