"""Project36HROM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path,include
from django.views.generic import TemplateView
from Admin import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('login/', TemplateView.as_view(template_name='admin/admin_login_page.html'), name='login'),
    path('kkk/', views.login, name = 'kkk'),
    path('addemp/', TemplateView.as_view(template_name='admin/add_employee_page.html'), name='addemp'),
    path('saveemp/', views.SaveEmp.as_view(), name='saveemp'),
    path('viewemp/', views.ViewEmp.as_view(), name='viewemp'),
    path('updateemp/', views.updateemp, name='updateemp'),
    path('empupdate/', views.empupdate, name='empupdate'),
    path('updated/', views.updated, name='updated'),
    path('deleteemp/',views.Deleteemp.as_view(), name='deleteemp'),
    path('delete_a/', views.deleted, name='delete_a'),
    path('logout/', views.logout, name='logout')

]


