from django import forms


class SignupForm(forms.Form):
	username = forms.CharField(label="使用者名稱", max_length=100)
	password = forms.CharField(label="密碼", max_length=100)
	email = forms.EmailField(label="電子郵件")


class LoginForm(forms.Form):
	username = forms.CharField(label="使用者名稱", max_length=100)
	password = forms.CharField(label="密碼", max_length=100)