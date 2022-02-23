import imp
from django.shortcuts import render
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
