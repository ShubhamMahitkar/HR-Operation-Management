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
from django.urls import path
from django.views.generic import TemplateView
from Interviewer import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('interview_login/', TemplateView.as_view(template_name='interview/interview_login.html'), name='interview_login'),
    path('interview_logincheck/', views.interview_logincheck, name='interview_logincheck'),
    path('assign_interview/', views.assignInterview, name='assign_interview'),
    path('save_interview/', views.save_interview, name='save_interview'),
    path('logout/', views.logout, name='logout')


]
