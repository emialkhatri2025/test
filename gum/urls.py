from django.urls import path

from gum import views

urlpatterns = [
    path('gum/',views.home,name='homepage',),

]
