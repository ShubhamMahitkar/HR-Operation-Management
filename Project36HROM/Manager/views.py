from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View
from Manager.forms import NewInterviewSchForm
from Manager.models import NewRecruitModel
from Manager.forms import NewRecruitForm
from Applicant.models import ApplicationModel


def manager_logincheck(request):
    unm = request.POST['username']
    pas = request.POST['pass']
    if unm == 'manager' and pas == 'manager':
        request.session['status'] = True
        return render(request, 'manager/manager_home_page.html')
    else:
        messages.error(request,"Invalid username or password")
        return redirect('manager_login')


def logout(request):
    request.session['status'] = False
    return redirect('home')

class NewRecruit(View):
    def post(self, request):
        rf = NewRecruitForm(request.POST)
        if rf.is_valid():
            rf.save()
            return render(request, 'manager/recruitdata.html')
        else:
            rm = NewRecruitModel.objects.all()
            return render(request, 'manager/recruitdata.html', {"form": rf, "rm": rm})


    def get(self, request):
        rm = NewRecruitModel.objects.all()
        return render(request, 'manager/recruitdata.html', {"form": NewRecruitForm()})


class ModifyDetails(View):
    def get(self, request):
        x = NewRecruitModel.objects.all()
        return render(request, "manager/modify.html", {'data': x})

    def post(self, request):
        op = request.POST.get('opcode')
        x = NewRecruitModel.objects.get(opcode=op)
        return render(request, 'manager/modified.html', {"form": x})



class Modified(View):
    def post(self,request):
        op = request.POST["opc"]
        n1 = request.POST["n1"]
        n2 = request.POST["n2"]
        n3 = request.POST["n3"]
        n4 = request.POST["n4"]
        n5 = request.POST["n5"]
        n6 = request.POST["n6"]
        n7 = request.POST["n7"]
        n8 = request.POST["n8"]
        n9 = request.POST["n9"]
        NewRecruitModel.objects.filter(opcode=op).update(quali=n1, regstart=n2, agelim=n3, lastdate=n4, deptid=n5, nofposn=n6, desc=n7, resp=n8, cont=n9)
        # messages = {"mess":"successfully updated"}
        nrf = NewRecruitModel.objects.all()
        return render(request, 'manager/modify.html',{"model": nrf})


class DeleteRec(View):
    def get(self, request):
        nrf = NewRecruitModel.objects.all()
        return render(request, 'manager/delete_recruitment.html', {"data": nrf})

    def post(self, request):
        pass


def deleted(request):
    id=request.GET.get('id')
    nrf = NewRecruitModel.objects.filter(opcode=id)
    nrf.delete()
    return redirect('delete_recruit')



def back(request):
    return render(request, 'manager/manager_home_page.html')


class InterviewSchedule(View):
    def get(self,request):
        x = ApplicationModel.objects.all()
        return render(request, 'manager/interview_schedule.html', {"apmodel": x})



def add_interview_schedule(request):
    apid = request.POST.get('apmodel')
    return render(request, 'manager/add_interview_schedule.html', {"data":apid, "data2": NewInterviewSchForm()})


def save_interview_sch(request):
    ish = NewInterviewSchForm(request.POST)
    if ish.is_valid():
        ish.save()
        return redirect('interview_schedule')
    else:
        return render(request, 'manager/interview_schedule.html', {"data": NewInterviewSchForm()})



