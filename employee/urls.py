from django.urls import path

from employee import views

urlpatterns = [
    path('emp/',views.show,name='show',),
    path('empupdate/',views.updateemp, name='empupdate'),
    path('edit/<str:id>/', views.editemp, name='empEdit'),
    path('delete_emp/<str:id>/', views.delete, name='deleteEdit'),

]
