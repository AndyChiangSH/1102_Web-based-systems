from django.shortcuts import render
from .models import Post

# Create your views here.
def index(request):	
	posts = Post.objects.filter(enable=True).order_by("-pub_time")
	return render(request, "index.html", locals())

def write(request):
	success = True
	try:
		nickname = request.GET["nickname"]
		type = request.GET["type"]
		store_name = request.GET["store_name"]
		like = request.GET["like"]
		content = request.GET["content"]
	except Exception as e:
		success = False

	print(success)

	if success:
		if like == "T":
			like = True
		else:
			like = False
		new_post = Post.objects.create(nickname=nickname, type=type, store_name=store_name, like=like, content=content)
		new_post.save()

	return render(request, "write.html", locals())