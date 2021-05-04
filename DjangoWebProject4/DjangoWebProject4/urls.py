

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.shortcuts import render, redirect
from django.conf.urls import include
admin.autodiscover()


urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path(r'^(?P<parametr>\d+)/$', views.blogpost, name='blogpost'),
    path('contact/', views.contact, name='contact'),
    path('links/', views.links, name='links'),
    path('anketa/', views.anketa, name='anketa'),
    path('about/', views.about, name='about'),
    path('registration', views.registration, name='registration'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Log in',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]
