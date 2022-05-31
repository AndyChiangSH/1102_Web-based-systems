from django.db import models


# Create your models here.
class StoreType(models.Model):
	type_name = models.CharField(max_length=10)
	discription = models.CharField(max_length=50)

	def __str__(self):
		return self.type_name


class StoreInfo(models.Model):
	type = models.ForeignKey(StoreType, on_delete=models.CASCADE)
	store_name = models.CharField(max_length=20)
	AVG_PRICES = (
		("1", "0~100"),
		("2", "100~300"),
		("3", "300~800"),
		("4", "above 800"),
	)
	avg_price = models.CharField(max_length=1, choices=AVG_PRICES)
	rating = models.IntegerField()
	position = models.CharField(max_length=50)

	def __str__(self):
		return self.store_name


class FoodName(models.Model):
	store = models.ForeignKey(StoreInfo, on_delete=models.CASCADE)
	food_name = models.CharField(max_length=20)
	price = models.IntegerField()

	def __str__(self):
		return self.food_name