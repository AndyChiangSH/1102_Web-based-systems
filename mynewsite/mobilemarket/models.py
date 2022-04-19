from django.db import models


# Create your models here.
class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    url = models.URLField(default="http://mobiles.com")

    def __str__(self):
        return self.name


class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete=models.SET_NULL, null=True, verbose_name="型號")
    nickname = models.CharField(max_length=15, default="暱稱")
    description = models.TextField(default="無")
    year = models.PositiveIntegerField(default=2022)
    price = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nickname


class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    description = models.CharField(max_length=20, default="圖片")
    url = models.URLField(default="http://mobiles.com")

    def __str__(self):
        return self.description
