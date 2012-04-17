from django.http import HttpResponse, HttpResponseServerError
from django.shortcuts import render

from models import Link,Click
from utils import BASE10,BASE62,baseconvert

#This is our main link hash function 
def hash_link(request):
	link = Link.objects.get_or_create(link=request.POST['link']) #need to save the url first before we hash it
	if not link.link_short:
		link.link_short = baseconvert(str(link.pk),BASE10,BASE62)
		link.save()
	return render(request,'base.html',{'short_url':link.link_short},content_type="text/html")
	
