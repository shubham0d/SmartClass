from django.db import models

# Create your models here.
class notice(models.Model):
	SHIRT_SIZES = (
		('S', 'Small'),
		('M', 'Medium'),
		('L', 'Large'),
	)


	activity = models.CharField(max_length=20)
	typeof = models.CharField(max_length=40, null=True)
	date = models.DateField()
	lastdate = models.DateField()
	comment = models.CharField(max_length=500, null=True, blank=True)

	def __unicode__(self):
		return self.date