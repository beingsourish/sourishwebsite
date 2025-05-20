from django.shortcuts import render
from sourishtravellist.models import PlacesVisited

def home(request):
    places = PlacesVisited.objects.all()
    return render(request, 'HomePage.html', {'places': places})
