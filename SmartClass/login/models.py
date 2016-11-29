from django.db import models

# Create your models here.
class LoginInfo(models.Model):
	uname = models.CharField(max_length=20,unique=True, null=True)
	passwd = models.CharField(max_length=40, null=True)
	name = models.CharField(max_length=40, blank=True, null=True)
	rollno = models.CharField(max_length=8, primary_key=True,null=False)

	def __unicode__(self):
		return self.rollno