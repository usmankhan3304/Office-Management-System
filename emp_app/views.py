from django.shortcuts import render,redirect
from django.http import HttpResponse as hhtp
# Create your views here.
from emp_app.models import *
import datetime
from django.db.models import Q
def index(request):
    
    return render(request,"index.html")

def view_emp(request):
    data=Employee.objects.all()
    context={
        'data':data
    }
   
    return render(request,'view_emp.html',context)
def add_emp(request):

    data=Employee.objects.all()
    data1=Employee.objects.all()
    if request.method == "POST":
        data=request.POST
        first_name=data.get('first_name')
        last_name=data.get('last_name')
        department=data.get('department')
        salery=data.get('salery')
        bonus=data.get('bonus')
        role=data.get('role')
        phone=data.get('phone')
        hire_date=datetime.datetime.now().date()
        print(hire_date)

        Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            department_id = department,
            salery=salery,
            bonus=bonus,
            role_id=role,
            phone=phone,
            hire_date=hire_date
        )
        return redirect('/add_emp')
        
    return render(request, 'add_emp.html',{'data':data,'data1':data1})
def remove_emp(request,id=0):
    if id:
        try:
            querytset=Employee.objects.get(id=id)
            querytset.delete()
            return hhtp("emplyee removed successfully")
     
        except:
            return hhtp("please provide a valid id to remove the record !")
    data=Employee.objects.all()

    context={
        'data':data
    }
    return render(request, 'remove_emp.html',context)
def filter_emp(request):
    data=Employee.objects.all()

    if request.method == "POST":
        search=request.POST.get('search')
        print(search)
        if search is not None:
            data=data.filter(
                Q(first_name__icontains= search) | 
                Q (last_name__icontains= search)|
                Q(department__name__icontains=search) 
                |Q(role__name__icontains=search)
            )
            
            return render(request,'view_emp.html', {'data':data})    

    elif request.method=="GET":
     return render(request, 'filter_emp.html')  
    else:
        return hhtp("an Error occured")