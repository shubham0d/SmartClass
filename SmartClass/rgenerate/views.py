from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import LoginInfo
from django.db import connection
from django.http import HttpResponse
import random
# Create your views here.


def generate(request):
		rollnos = []
		if request.method == 'POST':
			cursor = connection.cursor()
			sql = "select rollno from rgenerate_rgrades1 where submit=True;"
			cursor.execute(sql)
			results = cursor.fetchall()
			for rows in results:
				rollnos.append(rows[0])
			
			#shuffle the rollnos
			random.shuffle(rollnos)
			submitno = len(rollnos)

			#appending for last rollnos
			rollnos.append(rollnos[0])
			rollnos.append(rollnos[1])
			rollnos.append(rollnos[2])
			for i in range(0,submitno):
				st1 = rollnos[i+1]
				st2 = rollnos[i+2]
				st3 = rollnos[i+3]
				sql = "update rgenerate_rgrades1 set st1 = '"+st1+"', st2 = '"+st2+"', st3 = '"+st3+"' where rollno = '"+rollnos[i]+"';"
				cursor.execute(sql)