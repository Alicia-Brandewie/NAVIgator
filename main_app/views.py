from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.views import LoginView


# class Home(LoginView):
#     template_name = 'home.html'
#FOR END


def home(request):
    return HttpResponse('<h1>NAVIgator</h1>')
    # template_name = 'home.html'


def about(request):
    return render(request, 'about.html')
    # return HttpResponse('<h1>ABOUT NAVIgator</h1>')


