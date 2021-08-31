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
from HRhead import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('hr_login/', TemplateView.as_view(template_name='hrhead/hrhead_login.html'), name='hr_login'),
    path('hr_logincheck/', views.hr_logincheck, name='hr_logincheck'),
    path('shortlisted/', views.shortlisted, name='shortlisted'),
    path('selected/', views.selected, name='selected'),
    path('rejected/', views.rejected, name='rejected'),
    path('logout/', views.logout, name='logout')

]
