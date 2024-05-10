from django.db import models

# Create your models here.

class Employee_Data(models.Model):
    c_ID = models.CharField(max_length=225 , primary_key=True)
    c_FirstName = models.CharField(max_length=225 , null=False)
    c_Lastname = models.CharField(max_length=225 ,null=False)
    c_Role = models.CharField(max_length=225)
    c_address = models.CharField(max_length=225)
    c_Email = models.CharField(max_length=225)
    c_Phone = models.CharField(max_length=225)
    c_Informarion = models.CharField(max_length=225)

    class Meta:
        db_table = "EmployeeData"



class Users_Data(models.Model):
    First_Name = models.CharField(max_length=225)
    Last_Name = models.CharField(max_length=225)
    Emai = models.CharField(max_length=225)
    Password = models.CharField(max_length=225)

    class Meta:
        db_table = "UsersData"

