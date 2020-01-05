from django.shortcuts import render

def home_view(request, *arg, **kwargs):
    return render(request, "home.html", {})