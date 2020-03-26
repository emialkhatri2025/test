from django.urls import path

from event import views

urlpatterns = [
    path('event/',views.eventHome,name='event_home'),
    path('sucess/',views.eventSucess,name='event_sucess'),

]
