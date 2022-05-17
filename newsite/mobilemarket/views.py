import imp
from itertools import product
from django.shortcuts import render
from .models import Product, PPhoto

# Create your views here.
def index(request):
    products = Product.objects.all()

    return render(request, "mobile/index.html", {"products": products})


def detail(request, id):
    try:
        product = Product.objects.get(id=id)
        images = PPhoto.objects.filter(product=product)
    except:
        pass

    return render(request, "mobile/detail.html", locals())