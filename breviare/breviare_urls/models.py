from django.db import models

# Create your models here.
 class Link(models.Model):
	link = models.URLField(max_length=500)
	link_short = models.URLField(max_length=500) #our shortend URL
	created_on = models.DateTimeField(auto_now=True)
	
	def __unicode__(self):
		return self.link


class Click(models.Model): #Stats and Analytics pertaining to the click of a link
	link = models.ForeignKey(Link)
	clicked_on = models.DateTimeField(auto_now=True) #so when was it clicked?
	
	def __unicode__(self): 
		return self.link
	#def total_clicks(self): # add up all our clicks : o
	