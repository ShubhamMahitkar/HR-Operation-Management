from django.shortcuts import render,redirect
from django.contrib import messages
from Interviewer.forms import NewInterviewForm
from Applicant.models import ApplicationModel


def assignInterview(request):
    apid = request.POST.get('apmodel')
    return render(request, 'interview/assign_interview.html', {"data":apid, "data2": NewInterviewForm()})


def save_interview(request):
    inf = NewInterviewForm(request.POST)
    if inf.is_valid():
        inf.save()
        return redirect('assign_interview')
    else:
        return render(request, 'interview/assign_interview.html', {"data2": NewInterviewForm})


def interview_logincheck(request):
    unm = request.POST['username']
    pas = request.POST['pass']
    if unm == 'interview' and pas == 'interview':
        request.session['status'] = True
        x = ApplicationModel.objects.all()
        return render(request, 'interview/interview_home_page.html', {"apmodel": x})
    else:
        messages.error(request,"Invalid username or password")
        return redirect('interview_login')


def logout(request):
    del request.session['status']
    return redirect('home')

