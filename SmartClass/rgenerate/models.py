from django.db import models

# Create your models here.
class rgrades(models.Model):
	rollno = models.CharField(max_length = 10)
	submit =  models.BooleanField(default=False)
	st1 = models.CharField(max_length = 10, null=True)
	st2 = models.CharField(max_length = 10, null=True)
	st3 = models.CharField(max_length = 10, null=True)
	grd1 = models.CharField(max_length = 2, null=True)
	grd2 = models.CharField(max_length = 2, null=True)
	grd3 = models.CharField(max_length = 2, null=True)
	def __unicode__(self):
		return self.rollno