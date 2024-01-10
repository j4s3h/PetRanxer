"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from petlandiasimple.views import CreateMedicalRecord, DisplayMedicalRecordViewsIndiv, EditMedicalRecords, DeleteMedicalRecords, DisplayMedicalRecordsViews, LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path ('v1p0/create_medical_history/' , CreateMedicalRecord.as_view(), name= 'create_medical_history'),
    path ('v1p0/display_medical_history/' , DisplayMedicalRecordsViews.as_view(), name= 'get_medical_history'),
    path ('v1p0/delete_medical_history/<pk>/', DeleteMedicalRecords.as_view(), name = 'delete_medical_history'),
    path ('v1p0/edit_medical_record/<pk>/',EditMedicalRecords.as_view(), name = 'edit_medical_record'),
    path ('v1p0/display_medical_record/<pk>/',DisplayMedicalRecordViewsIndiv.as_view(), name = 'edit_medical_record'),
    path ('v1p0/login/',LoginView.as_view(), name = 'login')
]
