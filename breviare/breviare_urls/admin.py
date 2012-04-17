from models import Link,Click
from django.contrib import admin

class LinkAdmin(admin.ModelAdmin):	
	list_display = ('link','link_short','created_on','created_by')
	search_fields = ['link','link_short']
		
admin.site.register(Link, LinkAdmin)