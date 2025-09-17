from django.shortcuts import render
from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trip

from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

#__________Public Views__________#

class Home(LoginView):
    template_name = 'home.html'

# def home(request):
#     return render(request, 'home.html')
#     # return HttpResponse('<h1>NAVIgator</h1>')
#     # template_name = 'home.html'

def about(request):
    return render(request, 'about.html')
    # return HttpResponse('<h1>ABOUT NAVIgator</h1>')

#__________Authorization__________#

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )

#__________Athorized-only Views__________#

def trip_index(request):
    trips = Trip.objects.all()
    return render(request, 'trips/index.html', {'trips': trips})

def trip_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    return render(request, 'trips/detail.html', {'trip': trip})

class TripCreate(CreateView):
    model = Trip
    fields = '__all__'
    success_url = '/trips/'
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class TripUpdate(UpdateView):
    model = Trip
    fields = '__all__'

class TripDelete(DeleteView):
    model = Trip
    success_url = '/trips/'