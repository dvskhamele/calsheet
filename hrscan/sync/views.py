from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post
from . caltosheet import main

def home(request):
	if request.method == "POST":
		from . caltosheet import main
		main()
	return render(request,'sync/base1.html')