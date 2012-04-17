from django.db import models


# Create your models here.
class Link(models.Model):
	link = models.CharField(max_length=500)
	link_short = models.CharField(max_length=500,blank = True, null = True) #our shortend URL 
	created_on = models.DateTimeField(auto_now=True)
	created_by = models.CharField(max_length=50) #IP address for now - In user auth model for the future would be user object
	
	def __unicode__(self):
		return self.link
	
	def total_clicks(self):
		link_clicks = Click.objects.filter(link=self.link)
		return link_clicks #return all clicks of a link (all time)


class Click(models.Model): #Stats and Analytics pertaining to the click of a link
	link = models.ForeignKey(Link)
	clicked_on = models.DateTimeField(auto_now=True) #so when was it clicked?
	clicked_by = models.CharField(max_length=50) # Who clicked me
	refer = models.URLField(max_length=500, default="Direct") #whats the website or system that refered - Could be Direct 
	location = models.CharField(max_length=200) #general location Not specific 
	def __unicode__(self): 
		return self.link+" Clicks"
	
		
	