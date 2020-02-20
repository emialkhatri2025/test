from django.shortcuts import render, redirect
from employee.models import Demployee
from employee.forms import employee_forms


def show(request):
    employee_show = Demployee.objects.all()
    return render(request, 'employee/show.html',{'employee_show':employee_show})

def updateemp(request):
    employee_update = employee_forms(request.POST or None)
    if employee_update.is_valid():
        employee_update.save()
        return redirect('show')
    return render(request,'employee/update.html',{'employee_update':employee_update})

def editemp(request, id):
    #emp_id = int(emp_id)
    emp_sel = Demployee.objects.get(id=id)
    employee_update = employee_forms(request.POST or None, instance=emp_sel)
    if employee_update.is_valid():
        employee_update.save()
        return redirect('show')
    return render(request,'employee/update.html',{'employee_update':employee_update,"emp_sel":emp_sel})

def delete(request, id):
    delete_iteams = Demployee.objects.get(id=id)
    delete_iteams.delete()
    return redirect('show')
    return render(request, 'employee/show.html', {'delete_iteams':delete_iteams})
