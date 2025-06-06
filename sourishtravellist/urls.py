from django.urls import path
from sourishtravellist import views
urlpatterns = [
    path('',views.index,name='index'),
    path('indexstates/', views.indexstates, name='states'),
    path('<int:place_id>', views.place_details, name='place_details'),
    path('api/placeslist/', views.places_api, name='places_api'),
    path('placeslist/', views.places_aboutme, name='places_aboutme'),
    path('signup/', views.signup, name='signup'),
    path('dashboard/', views.dashboard, name='admin_login'),
    path('earlyLife/', views.earlyLife, name='earlyLife'),
    path('schooling/', views.schooling, name='schooling'),
    path('college/', views.college, name='college'),
    path('career/', views.career, name='career'),
path('journeytousa/', views.journeytousa, name='journeytousa')

]