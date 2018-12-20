from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post

def home(request):
	if request.method == "POST":
		from . caltosheet import main
		main()
	return render(request,'sync/base1.html')