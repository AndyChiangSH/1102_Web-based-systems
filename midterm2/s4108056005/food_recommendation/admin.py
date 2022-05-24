from django.contrib import admin
from .models import StoreType, StoreInfo, FoodName

# Register your models here.
admin.site.register(StoreType)
admin.site.register(StoreInfo)
admin.site.register(FoodName)