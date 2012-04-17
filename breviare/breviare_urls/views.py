from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render

from settings import BASE_URL
from models import Link,Click
from utils import BASE10,BASE62,baseconvert

#This is our main link hash function 
def shorten_link(request):
	link = Link.objects.get_or_create(link=request.GET['link']) #need to save the url first before we hash it
	print link
	if not link[0].link_short:
		link[0].link_short = baseconvert(link[0].pk,BASE10,BASE62)
		link[0].save()
	return render(request,'index.html',{'short_url':BASE_URL+link[0].link_short},content_type="text/html")
	
