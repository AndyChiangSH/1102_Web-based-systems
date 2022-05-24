from django.db import models
from django.utils import timezone

# Create your models here.
class Menu(models.Model):
	CATEGORY = (
		("R", "Rice"),
		("N", "Noodles"),
		("D", "Dumpling"),
		("d", "dishes"),
	)
	category = models.CharField(max_length=1, choices=CATEGORY)
	name = models.CharField(max_length=200)
	is_spicy = models.BooleanField(default=False)
	price = models.PositiveIntegerField()
	pub_time = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ("-pub_time", )

	def __str__(self):
		return self.name


class MyUser(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.EmailField()

	def __str__(self):
		return self.username