from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect

from .forms import LoginForm, RegisterForm

class RegisterView(CreateView):
    form_class      = RegisterForm
    template_name   = 'register.html'
    success_url     = '/login/'

def logout_view(request, *arg, **kwargs):
    logout(request)
    return render(request, 'logout.html', {})