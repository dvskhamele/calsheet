from django.shortcuts import render
from django.http import HttpResponse
#from .models import Post

def home(request):
	if request.method == "POST":
		try:
			if request.POST['caltosheet'] == "1":
				from . caltosheet import main
		except:
			if request.POST['csurgeryrunning'] == "1":
				from . csurgeryrunning import main
		main()
	return render(request,'sync/base1.html')