from django.shortcuts import render
# from django.http import HttpResponse
from django.contrib.auth.views import LoginView


def Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')