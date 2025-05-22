from django.http import HttpResponse
from django.shortcuts import render, redirect
from sourishtravellist.models import PlacesVisited,Places,Userdetails
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

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')

        # Check if email already exists
        if Userdetails.objects.filter(email=email).exists():
            return HttpResponse("Email already registered.")

        # Save to database
        Userdetails.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender
        )
        return HttpResponse("Thank you for signing up! Our team will reach out to You.")
    else:
        return redirect('/')

@api_view(['GET'])
def places_api(request):
    places = PlacesVisited.objects.all()
    serializer = PlacesVisitedSerializer(places, many=True)
    return Response(serializer.data)