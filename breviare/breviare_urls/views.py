from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render

from settings import BASE_URL
from models import Link,Click
from utils import BASE10,BASE62,baseconvert

#This is our main link hash function 
def shorten_link(request):
	submit_link = request.GET['link']
	if 'http://' not in submit_link:    #could be expanded to https 
		submit_link = 'http://'+submit_link
	link = Link.objects.get_or_create(link=submit_link,created_by=request.META.get("REMOTE_ADDR","")) #need to save the url first before we hash it because we are basing the hash on the unique ID
	if not link[0].link_short: #Get OR CREATE returns a tuple of the object and a boolean value  - highlighting the object here
		link[0].link_short = BASE_URL+baseconvert(link[0].pk,BASE10,BASE62)
		link[0].save()
	return render(request,'index.html',{'short_url':link[0].link_short},content_type="text/html") #BASE_URL from settings file
	
#What happens when we click on a link :o 
def link_click(request):
	try: #Does this link we have clicked on exist?
		short_link = Link.objects.get(link_short=request.GET['link'])
	except:
		return render(request,'nolink.html',content_type="text/html")
	
	click = Click.objects.create(link=short_link,clicked_by=request.META.get("REMOTE_ADDR","")) #makes a link
	return HttpResponseRedirect(short_link.link)

		
	#figuring out what meta gives you what kind of data	
	print request.META.get("HTTP_REFERER","")
	print request.META.get("HTTP_USER_AGENT","")
	print 'add'+request.META.get("REMOTE_ADDR","")
	print request.META.get("REMOTE_HOST","")
	