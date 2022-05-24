from django.contrib import admin
from .models import Menu, MyUser

# Register your models here.
class MenuAdmin(admin.ModelAdmin):
	list_display = ("name", "category", "price")

admin.site.register(Menu, MenuAdmin)
admin.site.register(MyUser)