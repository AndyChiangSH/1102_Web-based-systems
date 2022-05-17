from email import message
import re
from django.shortcuts import render, redirect
from board import models
from . import forms
from django.contrib.sessions.models import Session
from django.contrib import messages

# Create your views here.
def index(request):
    try:
        if "username" in request.session:
            username = request.session["username"]
            useremail = request.session["useremail"]
    except:
        pass

    return render(request, "board/index.html", locals())

def login(request):
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            name = request.POST["name"]
            password = request.POST["password"]
            try:
                user = models.User.objects.get(name=name)
                if user.password == password:
                    request.session["username"] = user.name
                    request.session["useremail"] = user.email
                    messages.add_message(request, messages.SUCCESS, "成功登入～")
                    return redirect("/board/")
                else:
                    messages.add_message(request, messages.WARNING, "密碼錯誤！")
            except:
                messages.add_message(request, messages.WARNING, "找不到使用者！")
        else:
            messages.add_message(request, messages.INFO, "請檢查輸入欄位！")   
    else:
        login_form = forms.LoginForm()

    return render(request, "board/login.html", locals())


def logout(request):
    if "username" in request.session:
        Session.objects.all().delete()
        return redirect("/board/login")

    return redirect("/board/")


def userinfo(request):
    try:
        if "username" in request.session:
            username = request.session["username"]
            useremail = request.session["useremail"]
            # userinfo = models.User.objects.get(name=username)
        else:
            redirect("/board/login")
    except:
        pass

    return render(request, "board/userinfo.html", locals())


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