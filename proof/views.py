from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html",{})


def contacts_view(request, *args, **kwargs):
    return render(request, "contacts.html",{})


def about_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "This is about us",
        "my_number": 123,
        "my_list": [1,2,3,6,852,84,5874,878,54,8,"jjj"],
    }
    return render(request, "about.html",my_context)


def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})
