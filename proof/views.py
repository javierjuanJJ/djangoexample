from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return HttpResponse("<h1>Hellow World</h1>")


def contacts_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contacts view</h1>")


def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About view</h1>")


def social_view(request, *args, **kwargs):
    return HttpResponse("<h1>Social view</h1>")
