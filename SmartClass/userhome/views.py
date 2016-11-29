from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection

# Create your views here.
max=0
min=0
runno=0
nomore=0
user_rollno=""
#activity=0
def notify(request):
	global max
	global min
	global runno
	global nomore
	i=0
	j=0
	id1=[]
	activity1=[]
	typeof1=[]
	date1=[]
	lastdate1=[]
	comment1=[]
	path1=[]
	topic1=[]
	id2=[]
	activity2=[]
	typeof2=[]
	date2=[]
	lastdate2=[]
	comment2=[]
	path2=[]
	topic2=[]
	id3=[]
	activity3=[]
	typeof3=[]
	date3=[]
	lastdate3=[]
	comment3=[]
	path3=[]
	topic3=[]
	activity=[]
	typeof=[]
	date=[]
	lastdate=[]
	comment=[]
	path=[]
	topic=[]
	r=[]
	ftext=[]
	ftext2=[]
	ftext3=[]
	ftext4=[]

	if 'user' in request.COOKIES:
		print "jkhkjh"
		print request.COOKIES['user']
		luser = request.COOKIES['user']
		if luser =='':
			response=HttpResponseRedirect('/')
			return response
		#else:

		cursor = connection.cursor()
		sql = "SELECT COUNT(*) FROM userhome_notice;"
		cursor.execute(sql)
		results = cursor.fetchall()
		for rows in results:
			length=rows[0]

		###################for notification#####################

		if runno==0: #if page loads first time
			max=int(length)
		if length>10:
			min=int(length-10);
			sql = "SELECT * from userhome_notice where id between "+str(min)+" and "+str(max)+" order by id desc;"
			max=min;
			runno=1

		else:
			sql = "SELECT * from userhome_notice where id between 0 and "+str(max)+" order by id desc;"
			runno=1
			nomore=1	#all result are shown

		cursor.execute(sql)
		results = cursor.fetchall()
		for rows in results:
			activity.append(rows[1])
			typeof.append(rows[2])
			date.append(rows[3])
			lastdate.append(rows[4])
			comment.append(rows[5])
			path.append(rows[6])
			topic.append(rows[7])
			j=j+1

		print activity
		print date
		for c in activity:

			if c=='U': #if it is upload
				line1="<li><h2>Topic:"+str(topic[i])+"</h2></br>"
				line2 = 'Faculty has uploaded a '+str(typeof[i])+''
				line3 = '<a href="'+str(path[i])+'"><i>'+str(path[i])+'</i></a>'
				line4 = "<span>Last Date:</span>"+str(lastdate[i])+"</br>"

				line6 = "<span>Comment:</span>"+str(comment[i])+""
				line5 = "<p><span>Date:"+str(date[i])+"</span></p></li>"
				ftext.append(line1+line2+line3+line4+line6+line5)
			elif c=='C': #if it is comment
				line1="<li><h2>Topic:"+str(topic[i])+"</h2></br>"
				line3 = '<a href="'+str(path[i])+'"><i>'+str(path[i])+'</i></a>'

				line6 = "<span>Comment:</span>"+str(comment[i])+""
				line5 = "<p><span>Date:"+str(date[i])+"</span></p></li>"
				ftext.append(line1+line3+line6+line5)

			i=i+1

		################notifications end##################

		################notes section######################
		sql = "SELECT * FROM userhome_notice where typeof='V' or typeof='N' ORDER BY id desc LIMIT 10;"
		cursor.execute(sql)
		results = cursor.fetchall()
		for rows in results:
			id1.append(rows[0])
			activity1.append(rows[1])
			typeof1.append(rows[2])
			date1.append(rows[3])
			lastdate1.append(rows[4])
			comment1.append(rows[5])
			path1.append(rows[6])
			topic1.append(rows[7])
		k=0
		for c in activity1:
				line1="<li><h2>Topic:"+str(topic1[k])+"</h2></br>"
				line2 = 'Faculty has uploaded a '+str(typeof1[k])+''
				line3 = '<a href="'+str(path[k1])+'"><i>'+str(path[k1])+'</i></a>'
				line4 = "<span>Last Date:</span>"+str(lastdate1[k])+"</br>"

				line6 = "<span>Comment:</span>"+str(comment1[k])+""
				line5 = "<p><span>Date:"+str(date1[k])+"</span></p></li>"
				ftext2.append(line1+line2+line3+line4+line6+line5)
				k=k+1

		###############end notes############

		###############assingnment section#############
		sql = "SELECT * FROM userhome_notice where typeof='A' ORDER BY id desc LIMIT 10;"
		cursor.execute(sql)
		results = cursor.fetchall()
		for rows in results:
			id2.append(rows[0])
			activity2.append(rows[1])
			typeof2.append(rows[2])
			date2.append(rows[3])
			lastdate2.append(rows[4])
			comment2.append(rows[5])
			path2.append(rows[6])
			topic2.append(rows[7])

		k2=0
		for c in activity2:
				line1="<li><h2>Topic:"+str(topic2[k2])+"</h2></br>"
				line2 = 'Faculty has uploaded a '+str(typeof2[k2])+''
				line3 = '<a href="'+str(path[k2])+'"><i>'+str(path[k2])+'</i></a>'
				line4 = "<span>Last Date:</span>"+str(lastdate2[k2])+"</br>"

				line6 = "<span>Comment:</span>"+str(comment2[k2])+""
				line5 = "<p><span>Date:"+str(date2[k2])+"</span></p></li>"
				ftext3.append(line1+line2+line3+line4+line6+line5)
				k2=k2+1

		#############end assingnment##################

		#############notice section##################
		sql = "SELECT * FROM userhome_notice where activity='C' ORDER BY id desc LIMIT 10;"
		cursor.execute(sql)
		results = cursor.fetchall()
		for rows in results:
			id3.append(rows[0])
			activity3.append(rows[1])
			typeof3.append(rows[2])
			date3.append(rows[3])
			lastdate3.append(rows[4])
			comment3.append(rows[5])
			path3.append(rows[6])
			topic3.append(rows[7])
		k3=0
		for c in activity3:
			line1="<li><h2>Topic:"+str(topic3[k3])+"</h2></br>"
			line3 = '<a href="'+str(path[k3])+'"><i>'+str(path[k3])+'</i></a>'

			line6 = "<span>Comment:</span>"+str(comment3[k3])+""
			line5 = "<p><span>Date:"+str(date3[k3])+"</span></p></li>"
			ftext4.append(line1+line3+line6+line5)
			k3=k3+1
		return render(request, 'home/index.html', {'feeds':ftext, 'notes':ftext2, 'assing':ftext3, 'notice':ftext4, 'luser':luser} )

	else:
		return HttpResponseRedirect('/')





#quizing starts here
def quiz(request):
	quizno=[]
	date=[]
	topic=[]
	lastdate=[]
	path=[]
	ftext=[]
	global user_rollno
	if 'user' in request.COOKIES:
		print request.COOKIES['user']
		luser = request.COOKIES['user']
		if luser =='':
			response=HttpResponseRedirect('/')
			return response
		cursor = connection.cursor()
		sql = "select * from userhome_quiz order by quizno desc;"
		cursor.execute(sql)
		results = cursor.fetchall()
		for rows in results:
			quizno.append(rows[1])
			date.append(rows[2])
			topic.append(rows[3])
			lastdate.append(rows[4])
			path.append(rows[5])

		m=0
		for c in quizno:
				line1="<li><h2>Quiz No:"+str(quizno[m])+"</h2></br>"
				line2='Topic: '+str(topic[m])+''
				line3 = "<a href=""><i>"+str(path[m])+"</i></a>"
				line4 = "<span>Last Date:</span>"+str(lastdate[m])+"</br>"
				line5 = "<p><span>Date:"+str(date[m])+"</span></p></li>"
				ftext.append(line1+line2+line3+line4+line5)
				m=m+1
		if request.method == 'POST':
				#saving the grades submitted
				grade1 = request.POST['std1']
				grade2 = request.POST['std2']
				grade3 = request.POST['std3']
				#print grade1,grade2,grade3
				#print user_rollno
				if grade1!="oo":
					sql = "UPDATE rgenerate_rgrades1 SET grd1='"+grade1+"' WHERE rollno='"+user_rollno+"';"
					cursor.execute(sql)

				if grade2!="oo":
					sql = "UPDATE rgenerate_rgrades1 SET grd2='"+grade2+"' WHERE rollno='"+user_rollno+"';"
					cursor.execute(sql)
				if grade3!="oo":
					sql = "UPDATE rgenerate_rgrades1 SET grd2='"+grade2+"' WHERE rollno='"+user_rollno+"';"
					cursor.execute(sql)

		#cheking section starts here
		sql = "select rollno from login_logininfo where uname = '"+luser+"';"
		cursor.execute(sql)
		results = cursor.fetchall()
		#get the rollno first
		for rows in results:
			user_rollno = rows[0]
		#now get the random alloted students rollno
		sql = "select st1 from rgenerate_rgrades1 where rollno = '"+user_rollno+"';"
		cursor.execute(sql)
		results = cursor.fetchall()
		if results==(): #means he doesn't submitted
			return render(request, 'quiz/index.html',{'quizzez':ftext, 'luser':luser})
		else:
			for rows in results:
				st1 = rows[0]

			sql = "select st2 from rgenerate_rgrades1 where rollno = '"+user_rollno+"';"
			cursor.execute(sql)
			results = cursor.fetchall()
			for rows in results:
				st2 = rows[0]

			sql = "select st3 from rgenerate_rgrades1 where rollno = '"+user_rollno+"';"
			cursor.execute(sql)
			results = cursor.fetchall()
			for rows in results:
				st3 = rows[0]


			return render(request, 'quiz/index.html', {'quizzez':ftext, 'luser':luser, 'st1':st1, 'st2':st2, 'st3':st3 })

		return render(request, 'quiz/index.html',{'quizzez':ftext, 'luser':luser})
	else:
		return HttpResponseRedirect('/')



def contact(request):
	if 'user' in request.COOKIES:
		print request.COOKIES['user']
		luser = request.COOKIES['user']
		if luser =='':
			response=HttpResponseRedirect('/')
			return response

		return render(request, 'contact/index.html', {'luser':luser})
	else:
		return HttpResponseRedirect('/')
