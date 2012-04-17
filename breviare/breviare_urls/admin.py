from models import Link,Click
from django.contrib import admin

class LinkAdmin(admin.ModelAdmin):	
	list_display = ('link','link_short','created_on','created_by','total_clicks')
	search_fields = ['link','link_short']

class ClickAdmin(admin.ModelAdmin):
	list_display = ('link','clicked_on','clicked_by')
admin.site.register(Link, LinkAdmin)
admin.site.register(Click, ClickAdmin)