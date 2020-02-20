from django.urls import path

from crudetest import views

urlpatterns = [
    path('crude/',views.index,name='index',),
    path('index/',views.show,name = 'show'),
    path('delete/<int:id>/',views.delete_post, name = 'delete_post'),
    

]
