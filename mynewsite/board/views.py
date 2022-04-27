from cgitb import enable
from django.shortcuts import render
from board import models

# Create your views here.
def index(request):
    # try:
    #     user_id = request.GET["user_id"]
    #     user_pass = request.GET["user_pass"]
    #     byear = request.GET["byear"]
    #     fcolor = request.GET.getlist("fcolor")
    # except:
    #     user_id = None
    #     user_pass = None

    # if user_id == "Andy" and user_pass == "123456":
    #     verified = True
    # else:
    #     verified = False

    posts = models.Post.objects.filter(enabled=True).order_by("-pub_time")[:30]

    return render(request, "board/index.html", locals())


def new_post(request):
    moods = models.Mood.objects.all()
    years = range(1960, 2022)
    try:
        nickname = request.GET["nickname"]
        del_pass = request.GET["del_pass"]
        message = request.GET["message"]
        mood = request.GET["mood"]
        byear = request.GET["byear"]
    except:
        nickname = None
        alert = "欄位皆必填！"
    
    if nickname != None:
        mood = models.Mood.objects.get(status=mood)
        post = models.Post.objects.create(mood=mood, nickname=nickname, del_pass=del_pass, message=message, byear=byear)
        post.save()
        alert = "張貼成功！"

    return render(request, "board/new_post.html", locals())
