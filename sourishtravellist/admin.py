from django.contrib import admin
from sourishtravellist.models import *
# Register your models here.

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'place_city')

class PlacesAdminState(admin.ModelAdmin):
    list_display = ('id',  'place_state')

admin.site.register(Places,PlacesAdminState)
admin.site.register(PlacesVisited,PlacesAdmin)