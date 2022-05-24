from django.shortcuts import render
from .models import StoreType, StoreInfo, FoodName

# Create your views here.
def recommend(request, id=1, id2=0):
	types = StoreType.objects.all()
	try:
		type = StoreType.objects.get(id=id)
		stores = StoreInfo.objects.filter(type=type)
		if id2 != 0:
			store = StoreInfo.objects.get(id=id2)
			foods = FoodName.objects.filter(store=store)
	except Exception as e:
		raise e

	return render(request, "recommend.html", locals())