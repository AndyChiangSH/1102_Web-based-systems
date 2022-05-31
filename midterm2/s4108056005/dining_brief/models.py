from django.db import models

# Create your models here.
class Post(models.Model):
	TYPES = (
		("T", "Taiwanese"),
		("J", "Japanese"),
		("K", "Korean"),
		("E", "European"),
	)
	nickname = models.CharField(max_length=10)
	type = models.CharField(max_length=1, choices=TYPES)
	store_name = models.CharField(max_length=20)
	like = models.BooleanField(default=True)
	content = models.TextField(max_length=100)
	pub_time = models.DateTimeField(auto_now=True)
	enable = models.BooleanField(default=False)

	def __str__(self):
		return self.nickname

