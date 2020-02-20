from django.shortcuts import render, redirect
from first.models import tips_calculator
from django.template import loader
from first.forms import BookCreate
from first.models import Books
from django.http import HttpResponse
from first.models import test
from first.forms import TestForm


def upload_test(request):
    test_f = TestForm(request.POST or None)
    if test_f.is_valid():
        test_f.save()
        return redirect('test_show')
    return render(request, 'first/test.html', {'test_f': test_f})

def test_show(request):
    test_show = test.objects.all()
    #return redirect('test_show')
    return render(request, 'first/show1.html',{'test_show':test_show})

def delete(request, id):
    test_del = test.objects.get(pk=id)
    test_del.delete()
    return redirect('test_show')




def upload(request):
    form = BookCreate(request.POST or None)
    if form.is_valid():
        try:
            form.save()
            return redirect('index')
        except:
            pass
    else:
        form = BookCreate()
    return render(request,'first/index.html',{'form':form})

def index(request): #show the saved data
    shelf = Books.objects.all()

    return render (request, 'first/upload.html',{'shelf':shelf})

def edit(request, id):
    pass
    #shelf = Books.objects.get(id=id)
    #return render(request,'first/edit.html', {'shelfs': shelf})
