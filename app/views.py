from django.shortcuts import render, get_object_or_404 ,redirect
from app.models import Employee_Data, Users_Data
from django.http import HttpResponse

# Create your views here.
def Create_Record(request):
    if request.method == 'POST':
        c_id = request.POST.get('Id')
        c_FirstName = request.POST.get('FirstName')
        c_LastName = request.POST.get('LastName')
        c_Role = request.POST.get('Role')
        c_Address = request.POST.get('Address')
        c_Email = request.POST.get('Email')
        c_Phone = request.POST.get('Phone')
        c_AdditionalInformation = request.POST.get('AdditionalInformation')

        c_Record = Employee_Data.objects.create(
            c_ID=c_id,
            c_FirstName=c_FirstName,
            c_Lastname=c_LastName,
            c_Role=c_Role,
            c_address=c_Address,
            c_Email=c_Email,
            c_Phone=c_Phone,
            c_Informarion=c_AdditionalInformation,
        )
        return HttpResponse("Record created successfully.") 
    else:
        return render(request , 'index.html')



def Update_Recoed(request):
    if request.method == 'POST':
        u_id = request.POST.get('Uid')
        u_selecting = request.POST.get('Uselecting')
        u_updating = request.POST.get('Uupdating')

     
        try:
            u_Record = Employee_Data.objects.get(c_ID=u_id)

            if u_selecting == '1':
                u_Record.c_FirstName = u_updating
            elif u_selecting == '2':
                u_Record.c_Lastname = u_updating
            elif u_selecting == '3':
                u_Record.c_Role = u_updating
            elif u_selecting == '4':
                u_Record.c_address = u_updating
            elif u_selecting == '5':
                u_Record.c_Email = u_updating
            elif u_selecting == '6':
                u_Record.c_Phone = u_updating
            elif u_selecting == '7':
                u_Record.c_Informarion = u_updating
            else:
                return HttpResponse("Invalid selection.")
            
            u_Record.save()

            return HttpResponse("Record updated successfully.")
        except Employee_Data.DoesNotExist:
            return HttpResponse("Record not found.")
        

def Delete_Record(request):
    if request.method == 'POST':
        d_id = request.POST.get('IdDelete')

        try:
            Find_id = Employee_Data.objects.filter(c_ID=d_id)
            if Find_id.exists():
                deletion_count = Find_id.delete()
                return HttpResponse(f"Successfully deleted {deletion_count} records.")
            else:
                return HttpResponse("Record not found.")
        except Employee_Data.DoesNotExist:
            return HttpResponse("Record not found.")

def Read_Date(request ):
    find = request.GET.get('ReadData', None)
    try:
        if find:
            get_data = Employee_Data.objects.filter(c_ID=find).first()
            context = {'data' :get_data }

            return render(request, 'singleData.html', context)
        else:
            return HttpResponse("Record not found.")
    except:
         return HttpResponse("No ID provided.")
        


def Show_All(request):
    all_employees = Employee_Data.objects.all()
    if all_employees.exists():
        context = {'ShowData':all_employees}
        return render(request, 'totalData.html', context)
    else:
        return HttpResponse("No records found.")
    
def Delete_All(request):
    all_employess = Employee_Data.objects.all()
    if all_employess.exists():
        all_employess.delete()
        return HttpResponse("all records found.")
    else:
        return HttpResponse("No records found.")


# Get data to Excel Sheet

import pandas as pd

def Get_Data_to_Excel(request):
    # Fetch data from the database
    data = Employee_Data.objects.all().values()
    # Convert to DataFrame
    df = pd.DataFrame(data)

     # Convert DataFrame to Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="data.xlsx"'


    with pd.ExcelWriter(response, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Sheet1')

    return response



#users

def Login(request):
    if request.method == "POST":
        Emai = request.POST.get('Email') 
        Password = request.POST.get('Password')
    
        if Users_Data.objects.filter(Emai = Emai).exists():
            if Users_Data.objects.filter(Emai = Emai ,Password  = Password).exists():
                 return redirect('/Create_Record/')
            else:
                 return HttpResponse('you Password wrong')
        else:
             return HttpResponse(f'data is not  found')

    return render(request , 'login.html')

def Register(request):
    if request.method == 'POST':
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Emai = request.POST.get('Emai') 
        Password = request.POST.get('Password')

        
        if Users_Data.objects.filter(Emai = Emai ).exists():
            return HttpResponse(f'data is exist ')

        else:
            regester_user = Users_Data.objects.create(
            First_Name = First_Name,
            Last_Name = Last_Name,
            Emai = Emai,
            Password = Password
             )
            regester_user.save()
            
            return HttpResponse(f'data is found {First_Name}, {Last_Name} , {Emai} , {Password}')
    
    return render(request , 'register.html')


def LogOut(request):
    return redirect('/Register/')