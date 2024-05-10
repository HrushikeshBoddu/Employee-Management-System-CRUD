"""
URL configuration for ems project.

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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Create_Record/',views.Create_Record , name='Create'),
    path('Update_Recoed/' , views.Update_Recoed , name='Update'),

    path('Read_Date/', views.Read_Date, name='Read_Date'),
    path('Show_All/' , views.Show_All , name='ShowAll'),

    path('Delete_Record/' , views.Delete_Record , name='Delete' ),
    path('Delete_All/' , views.Delete_All , name='Delete_All'),


    # Excel root
     path('download-excel/', views.Get_Data_to_Excel, name='download-excel'),

     #users
     path('', views.Login , name='login'),
     path('Register/' , views.Register , name='Register'),
     path('LogOut/' , views.LogOut , name='LogOut')
]
