from django.urls import path

from first import views

urlpatterns = [
    path('',views.upload,name='index',),
    path('updated/', views.index, name='updated1'),
    path('test/', views.upload_test, name = 'upload_test'),
    path('d',views.test_show, name = 'test_show'),
    path('del/<int:id>/',views.delete, name= 'delete'),
]
