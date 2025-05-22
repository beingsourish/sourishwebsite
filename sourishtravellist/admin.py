from django.contrib import admin
from sourishtravellist.models import *
# Register your models here.

class PlacesAdmin(admin.ModelAdmin):
    list_display = ('id', 'place_name', 'place_city')

class PlacesAdminState(admin.ModelAdmin):
    list_display = ('id',  'place_state')

class userdetailsAdmin(admin.ModelAdmin):
    list_display = ('id',  'user_name' ,'password' ,'email' ,'first_name','last_name' ,'gender' )

admin.site.register(Places,PlacesAdminState)
admin.site.register(PlacesVisited,PlacesAdmin)
admin.site.register(Userdetails,userdetailsAdmin)