from django.urls import path
from sourishtravellist import views
urlpatterns = [
    path('',views.index,name='index'),
    path('indexstates/', views.indexstates, name='states'),
    path('<int:place_id>', views.place_details, name='place_details'),
    path('api/placeslist/', views.places_api, name='places_api'),
    path('placeslist/', views.places_aboutme, name='places_aboutme'),
]