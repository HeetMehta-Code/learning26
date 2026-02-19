from django.shortcuts import render, redirect
from .models import Employee
from .forms import updateForm   # import your ModelForm


def employeeList(request):
    employees = Employee.objects.all().order_by("id")
    return render(request, 'employeelist.html', {"employees": employees})


def updateEmployee(request, id):
    employee = Employee.objects.get(id=id)

    if request.method == "POST":
        form = updateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect("employeeList")
    else:
        form = updateForm(instance=employee)
        return render(request, "updateForm.html", {"form": form})
    
def deleteEmployee(request, id):
    Employee.objects.filter(id=id).delete()
    return redirect("employeeList")

def sortEmployee(request):
    employees = Employee.objects.all().order_by("salary")
    return render(request, "employeelist.html", {"employees": employees})

def dsortEmployee(request):
    employees = Employee.objects.all().order_by("-salary")
    return render(request, "employeelist.html", {"employees": employees})

def createEmployee(request):
    print(request.method)
    if request.method == "POST":
        form = updateForm(request.POST)
        form.save() 
        return redirect("employeeList")
    else:
       
        form = updateForm()      
        return render(request,"createEmployee.html",{"form":form})
 
