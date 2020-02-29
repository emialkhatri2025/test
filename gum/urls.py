from django.urls import path

from gum import views

urlpatterns = [
    path('gum/',views.home,name='homepage'),
    path('updategum/',views.home_post,name ='gumhomepost'),
    path('editgum/<str:id>/',views.home_edit,name='gumhomeedit'),
    path('deletegum/<str:id>/',views.home_delete,name='gumhomedelete'),

]
