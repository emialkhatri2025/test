from django.shortcuts import render, redirect
from django.core.mail import send_mail

def eventHome(request):
    first_name = request.POST.get('user_first_name')
    last_name = request.POST.get('user_last_name')
    emial_name = request.POST.get('user_email_name')
    total_name = request.POST.get('user_total_name')
    print(total_name)

    send_mail(
        'subject - Event Registration Django',
        'Hello' + 'thaks for comming',
        'test@example.com',
        [
            emial_name,
        ]
    )
    #return redirect('event_sucess')
    return render(request,'event/registration.html')

def eventSucess(request):
    return render(request,'event/sucess.html')
