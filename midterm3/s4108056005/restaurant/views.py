from django.shortcuts import render, redirect
from .models import Menu, MyUser
from django.http import Http404
from . import forms
from django.contrib import messages


# Create your views here.
def index(request, cate="Rice"):
	user_name = request.session["username"]
	# print("user_name:", user_name)
	if user_name == None:	# 未登入
		return redirect("/login/")

	CATEGORY = {
		"Rice": "R",
		"Noodles": "N",
		"Dumpling": "D",
		"dishes": "d",
	}
	try:
		items = Menu.objects.filter(category=CATEGORY[cate])
	except:
		items = None

	if items == None:
		return redirect("/")
	
	context = {
		"cate": cate,
		"items": items,
		"user_name": user_name,
	}

	return render(request, "index.html", context=context)


# 註冊
def signup(request):
	if request.method == "POST":	# POST
		form = forms.SignupForm(request.POST)	# 註冊表單
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]
			email = form.cleaned_data["email"]

			try:
				other_user = MyUser.objects.get(username=username)	# 看看有沒有其他使用者
			except:
				other_user = None

			if other_user == None:	# 沒有則新增
				user = MyUser.objects.create(username=username, password=password, email=email)
				user.save()
				# message = "註冊成功！"
				messages.add_message(request, messages.SUCCESS, "註冊成功！")
				return redirect("/login/")
			else:
				# message = "帳號已註冊！"
				messages.add_message(request, messages.WARNING, "帳號已註冊！")
		else:
			# message = "不可以漏填！"
			messages.add_message(request, messages.WARNING, "不可以漏填！")
	else:	# GET
		form = forms.SignupForm()

	return render(request, "signup.html", locals())


# 登入
def login(request):
	if request.method == "POST":	# POST
		form = forms.LoginForm(request.POST) # 登入表單
		if form.is_valid():
			username = form.cleaned_data["username"]
			password = form.cleaned_data["password"]

			success = False
			try:
				user = MyUser.objects.get(username=username)
				if user.password == password:	# 密碼相同
					request.session["username"] = username
					success = True
			except:
				pass

			if success:
				# message = "登入成功！"
				messages.add_message(request, messages.SUCCESS, "登入成功！")
				return redirect("/")
			else:
				# message = "帳號或密碼有誤！"
				messages.add_message(request, messages.WARNING, "帳號或密碼有誤！")
	else:	#GET
		form = forms.LoginForm()

	return render(request, "login.html", locals())


# 登出
def logout(request):
	try:
		request.session["username"] = None
	except:
		pass

	return redirect("/login/")


# 個人資料
def info(request):
	user_name = request.session["username"]
	if user_name == None:
		return redirect("/login/")

	user = MyUser.objects.get(username=user_name)

	return render(request, "info.html", locals())