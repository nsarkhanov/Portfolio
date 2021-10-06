from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('blog/', views.blog, name='blog'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact_me, name='contact'),

]