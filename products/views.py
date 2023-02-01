from django.shortcuts import render
from .models import Product
from .forms import ProductForm
# Create your views here.

def product_create_view(request):
    context = {}
    if request.method == "POST":
        title = request.POST.get('title')
    return render(request, "product/create.html", context)


def product_detail_view(request):
    obj = Product.objects.get(id = 1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description,
    # }

    context = {
        'objact': obj
    }
    return render(request, "product/detail.html", context)
