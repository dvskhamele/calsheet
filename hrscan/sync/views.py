from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post

def home(request):
	return render(request,'sync/base1.html')




