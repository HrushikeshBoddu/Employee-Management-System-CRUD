from django.contrib import admin

# Register your models here.
from .models import Employee_Data, Users_Data

admin.site.register(Employee_Data)

admin.site.register(Users_Data)
