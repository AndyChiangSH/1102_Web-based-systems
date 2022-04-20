from django.contrib import admin
from .models import Maker, Product, PModel, PPhoto


# Register your models here.
admin.site.register(Maker)
admin.site.register(Product)
admin.site.register(PModel)
admin.site.register(PPhoto)
