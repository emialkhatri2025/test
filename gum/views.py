from django.shortcuts import render,redirect


def home(request):
    return render(request, 'gum/home.html')
