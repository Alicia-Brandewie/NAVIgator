from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# from django.contrib.auth.views import LoginView


# class Home(LoginView):
#     template_name = 'home.html'
#FOR END



class Trip:
    def __init__(self, location, date):
        self.location = location
        self.date = date

trips = [
    Trip('Paris', 9/19/2024),
    Trip('Cairo', 5/15/2026),
    Trip('Sydney', 12/12/2023)
]


def home(request):
    return render(request, 'home.html')
    # return HttpResponse('<h1>NAVIgator</h1>')
    # template_name = 'home.html'


def about(request):
    return render(request, 'about.html')
    # return HttpResponse('<h1>ABOUT NAVIgator</h1>')

def trip_index(request):
    return render(request, 'trips/index.html', {'trips': trips})
