from django.http import HttpResponse
from django.shortcuts import render
from sourishtravellist.models import PlacesVisited,Places
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sourishtravellist.serializers import PlacesVisitedSerializer


# Create your views here.
def index(request):
    places=PlacesVisited.objects.all()
    return render(request, 'placesVisited/travelListPlacesHome.html', {'places': places})

def indexstates(request):
    placestates=Places.objects.all()
    return render(request, 'placesVisited/statesVisited.html', {'placestates': placestates})

def place_details(request, place_id):
    try:
     placedetails = PlacesVisited.objects.get(id=place_id)
     return render(request, 'placesVisited/placeDetails.html', {'placedetails': placedetails})
    except:
        return render(request, 'placesVisited/dataNotExists.html')

def places_aboutme(request):
    return render(request, 'placesVisited/AboutMe.html')


@api_view(['GET'])
def places_api(request):
    places = PlacesVisited.objects.all()
    serializer = PlacesVisitedSerializer(places, many=True)
    return Response(serializer.data)