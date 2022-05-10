from cgitb import enable
from pyexpat import model
from django.db import models

# Create your models here.
class Mood(models.Model):
    status = models.CharField(max_length=10, null=False)

    def __str__(self):
        return self.status


class Post(models.Model):
    mood = models.ForeignKey("Mood", on_delete=models.CASCADE)
    nickname = models.CharField(max_length=10, default="匿名者")
    message = models.TextField(null=False)
    del_pass = models.CharField(max_length=10)
    pub_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    byear = models.IntegerField(default=2022)

    def __str__(self):
        return self.message


class Contact(models.Model):
    CITYS = [
        ["TP", "Taipei"],
        ["TC", "TaiChung"],
        ["TN", "Tainan"],
        ["O", "Others"],
    ]
    name = models.CharField(max_length=50, default="匿名")
    city = models.CharField(max_length=50, choices=CITYS)
    school = models.BooleanField(default=False)
    email = models.EmailField()
    message = models.CharField(max_length=100)

    def __str__(self):
        return self.name