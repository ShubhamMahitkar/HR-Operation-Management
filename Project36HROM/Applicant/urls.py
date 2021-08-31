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
from django.conf.urls.static import static
from django.urls import path
from django.views.generic import TemplateView
from Applicant import views
from Project36HROM import settings

urlpatterns = [
    path('applicant_login/', TemplateView.as_view(template_name="applicant/applicant_home_page.html"), name='applicant-login'),
    path('sign-up/', views.ApplicationLogin.as_view(), name='applicant-loggedin'),
    path('registration-form/',views.ShowForm.as_view(),name='registration-form'),
    path('apply/', views.Apply.as_view(), name='apply')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)