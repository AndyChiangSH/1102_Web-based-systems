from django import forms
from .models import Post, Contact, Diary, Profile
from captcha.fields import CaptchaField

# class ContactForm(forms.Form):
#     CITYS = [
#         ["TP", "Taipei"],
#         ["TC", "TaiChung"],
#         ["TN", "Tainan"],
#         ["O", "Others"],
#     ]
#     user_name = forms.CharField(label="您的姓名", max_length=50, initial="匿名")
#     user_city = forms.ChoiceField(label="居住城市", choices=CITYS)
#     user_school = forms.BooleanField(label="自否在學中", required=False)
#     user_email = forms.EmailField(label="您的電子郵件")
#     user_message = forms.CharField(label="您的意見", widget=forms.Textarea)


class PostForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Post
        fields = ["mood", "nickname", "message", "del_pass"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["mood"].label = "心情"
        self.fields["nickname"].label = "暱稱"
        self.fields["message"].label = "留言"
        self.fields["del_pass"].label = "刪除密碼"
        self.fields["captcha"].label = "我不是機器人"


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "city", "school", "email", "message"]

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields["name"].label = "您的姓名"
        self.fields["city"].label = "居住城市"
        self.fields["school"].label = "自否在學中"
        self.fields["email"].label = "您的電子郵件"
        self.fields["message"].label = "您的意見"
        self.fields["message"].widget = forms.Textarea()


class LoginForm(forms.Form):
    name = forms.CharField(label="姓名", max_length=20)
    password = forms.CharField(label="密碼", max_length=20, widget=forms.PasswordInput())


class DateInput(forms.DateInput):
    input_type = "date"

class DiaryForm(forms.ModelForm):
    class Meta:
        model = Diary
        fields = ["budget", "weight", "note", "ddate"]
        widgets = {"ddate": DateInput(), }

    def __init__(self, *args, **kwargs):
        super(DiaryForm, self).__init__(*args, **kwargs)
        self.fields["budget"].label = "今日花費"
        self.fields["weight"].label = "今日體重"
        self.fields["note"].label = "留言內容"
        self.fields["ddate"].label = "留言日期"


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["height", "male", "website"]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["height"].label = "您的身高"
        self.fields["male"].label = "您是男生嗎？"
        self.fields["website"].label = "個人網站"