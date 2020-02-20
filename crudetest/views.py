from django.shortcuts import render, redirect
from crudetest.models import HR
from crudetest.forms import HRForm

def index(request): #post the data to the database
    #upload = HRForm(HR, fields=('empid','name','age'))
    #if request.method == 'POST':
    upload = HRForm(request.POST or None)
    if upload.is_valid():
        upload.save()
        return redirect('show')

    return render(request, 'crudetest/index.html', {'upload':upload})

def show(request):
     #to get the data for the database
    upload_get = HR.objects.all()
    return render(request,'crudetest/show.html',{'upload_get':upload_get})
def edit_post(request):
    pass
def delete_post(request,id):
    upload_delete = HR.objects.get(pk=id)
    if request.method == 'POST':
        upload_delete.delete()
    return redirect('show')
    #return render(request, 'crudetest/Ddlete.html', {'upload_delete':upload_delete})
