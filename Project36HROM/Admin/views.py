from django.shortcuts import render,redirect
from django.views.generic.base import View
from Admin.models import AdminModel
from Applicant.models import ApplicationModel
from django.contrib import messages

def login(request):

    unm = request.POST['username']
    pas = request.POST['pass']
    if unm == 'admin' and pas == 'admin':
        request.session['status'] = True
        return render(request, 'admin/admin_home_page.html')

    else:
        message = messages.error(request, "Invalid username or password")
        return render(request, 'admin/admin_login_page.html', {"message": message})


class SaveEmp(View):
    def post(self,request):
        empname = request.POST["t1"]
        password = request.POST["t2"]
        designation = request.POST["t3"]
        address = request.POST["t4"]
        contact = request.POST["t5"]
        email = request.POST["t6"]
        am=AdminModel(empname=empname, password=password, designation=designation, address=address, contact=contact, email=email)
        am.save()
        return render(request, 'admin/add_employee_page.html', {"message":"saved"})


class ViewEmp(View):
    def post(self,request):
        pass

    def get(self, request):
        am = AdminModel.objects.all()
        return render(request, 'admin/viewemp.html', {"data": am})


def updateemp(request):
    am = AdminModel.objects.all()
    return render(request, 'admin/updateview.html', {"data": am})


def empupdate(request):
    eid = request.GET["eid"]
    am = AdminModel.objects.get(id = eid)
    return render(request, 'admin/empupdate.html', {"data": am})


def updated(request):

    id = request.POST["id"]
    empname = request.POST["t1"]
    password = request.POST["t2"]
    designation = request.POST["t3"]
    address = request.POST["t4"]
    contact = request.POST["t5"]
    email = request.POST["t6"]
    am = AdminModel.objects.filter(id = id)
    am.update(empname=empname, password=password, designation=designation, address=address, contact=contact,
                    email=email)
    return render(request, 'admin/updateview.html', {"data":AdminModel.objects.all()})


class Deleteemp(View):
     def get(self, request):
         am = AdminModel.objects.all()
         return render(request, 'admin/deleteemp.html', {"data": am})

     def post(self, request):
         pass

def deleted(request):
    id=request.GET.get('id')
    nrf = AdminModel.objects.filter(id=id)
    nrf.delete()
    return redirect('deleteemp')


def logout(request):
    del request.session['status']
    return redirect('home')
