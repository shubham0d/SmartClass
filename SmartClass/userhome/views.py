from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection

# Create your views here.

def notify(request):
	return render(request, 'home/index.html' )