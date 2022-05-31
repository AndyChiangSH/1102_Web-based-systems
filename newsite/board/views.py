from django.shortcuts import render, redirect
from board import models
from . import forms
from django.contrib.sessions.models import Session
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        diaries = models.Diary.objects.filter(user=request.user).order_by("-ddate")

    return render(request, "board/index.html", locals())

def login(request):
    if request.method == "POST":
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            name = login_form.cleaned_data["name"]
            password = login_form.cleaned_data["password"]
            print(name, password)
            user = auth.authenticate(username=name, password=password)
            print("user:", user)
            if user != None:
                if user.is_active:
                    auth.login(request, user)
                    messages.add_message(request, messages.SUCCESS, "成功登入～")
                    return redirect("/board/")
                else:
                    messages.add_message(request, messages.WARNING, "帳號未啟用！")
            else:
                messages.add_message(request, messages.WARNING, "帳號或密碼錯誤！")
        else:
            messages.add_message(request, messages.INFO, "請檢查輸入欄位！")   
    else:
        login_form = forms.LoginForm()

    return render(request, "board/login.html", locals())


def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, "成功登出～")

    return redirect("/board/")


# 個人資料
@login_required(login_url="/board/login")
def userinfo(request):
    try:    # 取得使用者個人資料
        profile = models.Profile.objects.get(user=request.user)
    except: # 新增使用者
        profile = models.Profile(user=request.user)

    if request.method == "POST":
        form = forms.ProfileForm(request.POST, instance=profile)    # 接收表單
        if form.is_valid(): # 更新成功
            messages.add_message(request, messages.SUCCESS, "個人資料更新成功")
            form.save()
            return redirect("/board/userinfo")
        else:   # 更新失敗
            messages.add_message(request, messages.WARNING, "所有欄位皆必填！")
    else:
        form = forms.ProfileForm()

    return render(request, "board/userinfo.html", locals())


def posting(request):
    if request.method == "POST":
        diary = models.Diary(user=request.user)
        form = forms.DiaryForm(request.POST, instance=diary)
        if form.is_valid():
            messages.add_message(request, messages.SUCCESS, "留言成功")
            form.save()
            return redirect("/board/")
        else:
            messages.add_message(request, messages.WARNING, "所有欄位皆必填！")
    else:
        form = forms.DiaryForm()

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
