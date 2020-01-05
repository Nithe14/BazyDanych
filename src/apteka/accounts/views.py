from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse

from .forms import LoginForm, RegisterForm

class RegisterView(CreateView):
    form_class      = RegisterForm
    template_name   = 'register.html'
    success_url     = '/login/'
