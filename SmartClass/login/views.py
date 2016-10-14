from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import LoginInfo
from django.db import connection

#from .forms import NameForm

#Create your views here.

def index(request):
	# prepare a cursor object using cursor() method
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		cursor = connection.cursor()
		# Execute the SQL command
		sql = "select passwd from login_logininfo where uname='"+username+"';"
		cursor.execute(sql)
		results = cursor.fetchall()
		print results
		if results==():
			print "rollno not present"
			connection.close()
			return render(request, 'login/noroll.html')

		else:
			for rows in results:
				passwd=rows[0]
        	if password == passwd:
        		print "sucessfully login"
        		return HttpResponseRedirect('/home')


        	else:
        		print "wrong password"
        		return render(request, 'login/wrongp.html')

        	connection.close()
	

	return render(request, 'login/normal.html')


def success(request):
	return render(request, 'login/success.html')

def signup(request):
	
	if request.method == 'POST':
		
		username = request.POST['username']
		password = request.POST['password']
		rollno = request.POST['rollno']
		authid = request.POST['authid']
		

		cursor = connection.cursor()
		sql = "SELECT rollno FROM login_logininfo where rollno='%s'" %rollno
		cursor.execute(sql)
		results = cursor.fetchall()
		print results
		if results==():
			print "rollno not present"
			return render(request, 'signup/serror.html')



		else:
			print "rollno present"
			sql = "UPDATE login_logininfo SET uname='"+username+"', passwd='"+password+"' WHERE rollno='"+rollno+"';"
			cursor.execute(sql)
			# Commit your changes in the database
    		connection.commit()
    		return HttpResponseRedirect('/success')


	return render(request, 'signup/signup.html')


