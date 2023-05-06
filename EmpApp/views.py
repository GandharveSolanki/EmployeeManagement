from django.shortcuts import render,HttpResponse

from .models import Employee,Role,Department
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,"index.html")

def AllEmp(request):
    Detail=Employee.objects.all()
    context={
        'Detail':Detail
    }

    print(context)
    return render(request,"ViewAll.html",context)

def AddEmp(request):
    Detail=Department.objects.all()
    Detail2=Role.objects.all()
    context={
        'Detail':Detail,
        'Detail2':Detail2
    }

    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept1=request.POST['dept']
        role1=request.POST['role']
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        salary=int(request.POST['salary'])
        
        mydata = Department.objects.filter(name=dept1).values()
        roledata = Role.objects.filter(name=role1).values()
        # print(mydata)
        # print(mydata[0]['id'])
        # print(roledata)
        newEmp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=int(mydata[0]['id']),role_id=int(roledata[0]['id']),hire_date=datetime.now())
        newEmp.save()
    
    return render(request,"AddEmp.html",context)

def Remove(request,emp_id=0):
    if emp_id:
        try:
            employee_remove=Employee.objects.get(id=emp_id)
            employee_remove.delete()
            return HttpResponse("employee removed successfully")
        except:
            return HttpResponse("Please choose a valid id")
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(emps)
    return render(request,"RemoveEmp.html",context)

def Filter(request):
    return render(request,"FilterEmp.html")