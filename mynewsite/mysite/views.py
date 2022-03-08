from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


# Create your views here.
def about(request):
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>About me</title>
</head>
<body>
    <h2>School</h2>
    <hr>
    <p>
        Hi, I am Andy.
    </p>
</body>
</html>    
"""

    return HttpResponse(html)


def listing(request):
    html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Mobile Phones</title>
</head>
<body>
    <h2>List of mobile phones</h2>
    <hr>
    <table width=400 border=1 bgcolor='#ccffcc'>
        {}
    </table>
</body>
</html>   
"""
    SIZES = {
        "S": "Small",
        "M": "Medium",
        "L": "Large",
    }
    products = Product.objects.all()
    tags = "<tr><td>item number</td><td>brand name</td><td>price</td><td>size</td></tr>"
    for p in products:
        tags += f"<tr><td>{p.sku}</td>"
        tags += f"<td>{p.name}</td>"
        tags += f"<td>{p.price}</td>"
        tags += f"<td>{SIZES[p.size]}</td></tr>"

    return HttpResponse(html.format(tags))