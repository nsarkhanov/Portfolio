from django.http import HttpResponse, response
from django.shortcuts  import render
from django.core.mail import send_mail


def home(response):

    return render(response,'main/home.html',{})


def projects(response):
   return render(response,'main/projects.html',{})

def contact_me(request):
    if request.method=="POST":
        f_name=request.POST.get('full-name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        data={
            'name':f_name,
            'email':email,
            'message':message
        }
        message='''
        From:{}

        New message:{}
        '''.format(data['email'],data['message'])
        send_mail('From Website',message,'',['nsarkhanov@gmail.com'])
    return render(request,'main/contact.html',{})