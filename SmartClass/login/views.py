from django.shortcuts import render
from django.http import HttpResponseRedirect
#from .forms import NameForm

#Create your views here.

'''

	if request.method == 'POST':
		username = request.POST['username']
    	password = request.POST['password']
    	print request.POST
	else:
		return render(request, 'signup/signup.html')
'''

def index(request):
	return render(request, 'login/index.html')


def signup(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		rollno = request.POST['rollno']
		authid = request.POST['authid']
		print username,password,authid,rollno
		
	return render(request, 'signup/signup.html')


