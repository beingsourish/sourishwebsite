from django.http import HttpResponse
from django.shortcuts import render, redirect
from sourishtravellist.models import PlacesVisited,Places,Userdetails
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sourishtravellist.serializers import PlacesVisitedSerializer
from django.contrib import messages

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

        if Userdetails.objects.filter(email=email).exists():
            messages.warning(request, "Email already registered.")
            return redirect('/')

        Userdetails.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            gender=gender
        )

        messages.success(request, "Thank you for signing up! Our team will reach out to you shortly.")
        return redirect('/')
    else:
        return redirect('/')

def dashboard(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        userdetails = Userdetails.objects.all()
        if username == 'beingsourish' and password == 'Kolkata@1':

            return render(request, 'userdashboard.html', {'userdetails': userdetails})
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials or not authorized.'})
    return render(request, 'admin_login.html')
@api_view(['GET'])
def places_api(request):
    places = PlacesVisited.objects.all()
    serializer = PlacesVisitedSerializer(places, many=True)
    return Response(serializer.data)