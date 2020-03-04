from django.shortcuts import render,redirect
from gum.models import movies
from gum.models import movieType
from gum.forms import movie_forms
from django.core.paginator import Paginator

def home(request):
    movies_type = movies.objects.all()
    contex = {'movies_type':movies_type}

    return render(request, 'gum/home.html', contex)

def home_post(request):
    movies_post = movie_forms(request.POST or None)
    if movies_post.is_valid():
        movies_post.save()
        return redirect('homepage')
    contex = {'movies_post':movies_post}
    return render(request,'gum/homepost.html', contex)

def home_edit(request, id):
    movies_edit = movies.objects.get(id=id)
    movies_post = movie_forms(request.POST or None, instance=movies_edit)
    if movies_post.is_valid():
        movies_post.save()
        return redirect('homepage')
    contex = {'movies_post':movies_post}
    return render(request,'gum/homepost.html',contex)

def home_delete(request, id):
    movies_delete = movies.objects.get(id=id)
    movies_delete.delete()
    return redirect('homepage')
    contex = {'movies_delete':movies_delete}
    return render(request,'gum/homedelete.html',contex)
