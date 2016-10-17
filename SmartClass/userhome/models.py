from django.db import models

# Create your models here.
class notice(models.Model):
	WHAT_TYPE = (
		('C', 'Comment'),
		('U', 'Upload'),
	)
	UPLOAD_OF = (
		('L', 'Link'),
		('N', 'Notes'),
		('V', 'Videos'),
		('A', 'Assingnment')
	)

	activity = models.CharField(max_length=20, choices=WHAT_TYPE)
	typeof = models.CharField(max_length=40, null=True, choices=UPLOAD_OF)
	date = models.DateTimeField()
	Path = models.CharField(max_length=50, null=True, blank=True)
	Topic = models.CharField(max_length=100, default='New Update')
	lastdate = models.DateField(null=True)
	comment = models.CharField(max_length=500, null=True, blank=True)

	def __unicode__(self):
		return self.date


class quiz(models.Model):
	quizno = models.IntegerField()
	date = models.DateTimeField()
	Topic = models.CharField(max_length=100)
	lastdate = models.DateField()
	Path = models.CharField(max_length=200,null=True)


	def __unicode__(self):
		return self.quizno
