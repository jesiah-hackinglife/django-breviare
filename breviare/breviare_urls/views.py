from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.shortcuts import render

from settings import BASE_URL
from models import Link,Click
from utils import BASE10,BASE62,baseconvert

#This is our main link hash function 
def shorten_link(request):
	link = Link.objects.get_or_create(link=request.GET['link']) #need to save the url first before we hash it because we are basing the hash on the unique ID
	if not link[0].link_short: #Get OR CREATE returns a tuple of the object and a boolean value  - highlighting the object here
		link[0].link_short = BASE_URL+baseconvert(link[0].pk,BASE10,BASE62)
		link[0].save()
	return render(request,'index.html',{'short_url':link[0].link_short},content_type="text/html") #BASE_URL from settings file
	

def link_click(request):
	short_link = Link.objects.get(link_short=request.GET['link'])
	if short_link:
		click = Click.objects.create(link=short_link,clicked_by=request.META.get("REMOTE_ADDR",""))
		return HttpResponseRedirect(short_link.link)
	else:
		return render(request,'index.html',content_type="text/html")
		
		
	print request.META.get("HTTP_REFERER","")
	print request.META.get("HTTP_USER_AGENT","")
	print 'add'+request.META.get("REMOTE_ADDR","")
	print request.META.get("REMOTE_HOST","")
	