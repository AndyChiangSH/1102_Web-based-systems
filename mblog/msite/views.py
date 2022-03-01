from ast import Try
import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from datetime import datetime


# Create your views here.
def homepage(request):
    posts = Post.objects.all().order_by("-pub_date")
    now = datetime.now()

    return render(request, "index.html", locals())

    # post_list = list()

    # for i, post in enumerate(posts):
    #     post_list.append(f"No.{i}: {post.title}<hr>")
    #     post_list.append(f"<small>" + str(post.body.encode("utf-8").decode("utf-8")) + "</small><br><br>")

    # return HttpResponse(post_list)


def post(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            return render(request, "post.html", locals())
    except:
        return redirect("/")