from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Product
import random
from datetime import datetime


# Create your views here.
def index(request, tvno=0):
    tv_list = [
        {"name": "公視", "tvcode": "4Uc00FPs27M"},
        {"name": "華視", "tvcode": "wM0g8EoUZ_E"},
        {"name": "寰宇", "tvcode": "B7Zp3d6xXWw"},
        {"name": "台視", "tvcode": "xL0ch83RAK8"},
    ]
    now = datetime.now()
    hour = now.timetuple().tm_hour
    tv = tv_list[tvno]

    return render(request, "index.html", {"tv": tv, "now": now, "hour": hour})


def engtv(request, tvno=0):
    tv_list = [
        {"name": "Sky News", "tvcode": "Ns3JgHODbI4"},
        {"name": "Euro News", "tvcode": "sPgqEHsONK8"},
        {"name": "India News", "tvcode": "zLD7bC0u5ms"},
    ]
    now = datetime.now()
    tv = tv_list[tvno]

    return render(request, "engtv.html", {"tv": tv, "now": now})


def carlist(request, maker=0):
    car_maker = ['Ford', 'Honda', 'Mazda']
    car_list = [
        [
            {'model':'Fiesta', 'price': 203500},
            {'model':'Focus','price': 605000},
            {'model':'Mustang','price': 900000}
        ],
        [
            {'model':'Fit', 'price': 450000},
            {'model':'City', 'price': 150000},
            {'model':'NSX', 'price':1200000}
        ],
        [
            {'model':'Mazda3', 'price': 329999},
            {'model':'Mazda5', 'price': 603000},
            {'model':'Mazda6', 'price':850000}
        ],
    ]
    maker_name = car_maker[maker]
    cars = car_list[maker]

    return render(request, "carlist.html", locals())


def musics(request, musicno=0):
    musics = [
        {"name": "Lofi", "code": "5qap5aO4i9A"},
        {"name": "Jazz", "code": "b4y_sdzwPzI"},
        {"name": "Remix", "code": "Fn7YH_eiJ0c"},
    ]
    now = datetime.now()
    music = musics[musicno]

    return render(request, "musics.html", locals())


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