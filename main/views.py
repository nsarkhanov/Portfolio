from django.http import HttpResponse, response
from django.shortcuts  import render


def home(response):

    return render(response,'main/home.html',{})


def projects(response):
   return render(response,'main/projects.html',{})

def contact_me(response):
    return render(response,'main/contact.html',{})