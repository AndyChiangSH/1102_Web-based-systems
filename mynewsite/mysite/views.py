from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product
import random


# Create your views here.
def index(request):
    return render(request, "index.html")


def about(request, author_no=0):
    author_no = author_no
    quotes = ["AAA", "BBB", "CCC", "DDD", "EEE"]
    quote = random.choice(quotes)

    return render(request, "about.html", locals())


def listing(request, year=0, month=0, day=0):
    products = Product.objects.all()
    date = f"{year}/{month}/{day}"

    return render(request, "list.html", locals())


def display_detail(request, sku):
    try:
        p = Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404("Product not found.")

    return render(request, "detail.html", locals())