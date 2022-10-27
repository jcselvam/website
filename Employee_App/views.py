from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

def Get(request):
    employees = Employee.objects.all()
    return render(request,'show.html',{'employees':employees})

def Post(request):
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        print("post",form)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = EmployeeForm()
    return render (request,'index.html',{'form':form})                


def Update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,instance=employee)
    
    if form.is_valid():
        form.save()
        return redirect('/show')    
    return render(request,'edit.html',{'employee':employee})    

def Delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')
