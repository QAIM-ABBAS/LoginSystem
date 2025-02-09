from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    return render(request, template_name="authentication/index.html")


def signup(request):
    return render(request, template_name="authentication/signup.html")


def login(request):
    return render(request, template_name="authentication/login.html")


def logout(request):
    return HttpResponse("hello logout working!")
