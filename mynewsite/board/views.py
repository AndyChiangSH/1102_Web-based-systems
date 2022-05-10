from django.shortcuts import render, redirect
from board import models
from . import forms

# Create your views here.
def index(request, pid=None, del_pass=None):
    if pid and del_pass:
        try:
            post = models.Post.objects.get(id=pid)
        except:
            post = None
        
        if post:
            if post.del_pass == del_pass:
                post.delete()
                message = "刪除成功！"
            else:
                message = "刪除密碼錯誤！"

    posts = models.Post.objects.filter(enabled=True).order_by("-pub_time")[:30]

    return render(request, "board/index.html", locals())


def posting(request):
    moods = models.Mood.objects.all()
    years = range(1960, 2022)
    # try:
    #     nickname = request.POST["nickname"]
    #     del_pass = request.POST["del_pass"]
    #     message = request.POST["message"]
    #     mood = request.POST["mood"]
    #     byear = request.POST["byear"]
    # except:
    #     nickname = None
    #     alert = "欄位皆必填！"
    
    # if nickname != None:
    #     mood = models.Mood.objects.get(status=mood)
    #     post = models.Post.objects.create(mood=mood, nickname=nickname, del_pass=del_pass, message=message, byear=byear)
    #     post.save()
    #     alert = "張貼成功！"

    if request.method == "POST":
        form = forms.PostForm(request.POST)
        if form.is_valid():
            message = "留言成功"
            form.save()
            return redirect("/board/listing")
        else:
            message = "所有欄位皆必填！"
    else:
        form = forms.PostForm()

    return render(request, "board/posting.html", locals())


def listing(request):
    posts = models.Post.objects.filter(enabled=True).order_by("-pub_time")

    return render(request, "board/listing.html", locals())


def contact(request):
    if request.method == "POST":
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = "感謝來信"
            form.save()
        else:
            message = "請檢查輸入的欄位是否正確！"
    else:
        form = forms.ContactForm()
    
    return render(request, "board/contact.html", locals())