from django.shortcuts import render, redirect
# from datetime import datetime
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trip, Transportation_stretch
from .forms import DateForm, TransportationForm
from django.db import models



from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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
            return redirect('trip-index')
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
@login_required
def trip_index(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trips/index.html', {'trips': trips})

@login_required
def trip_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    # transportation_form = TransportationForm()
    return render(request, 'trips/detail.html', {
        'trip': trip,
        'transportation_form':TransportationForm
    })

class TripCreate(LoginRequiredMixin, CreateView):
    #First add of widget; didn't work
    # class Meta:
        model = Trip
        # fields = ['location', 'companion', 'emergency_contact', 'transportation', 'lodging', 'attractions', 'notes']
        form_class = DateForm
        def form_valid(self, form):
            form.instance.user = self.request.user
            return super().form_valid(form)
        

class TripUpdate(LoginRequiredMixin, UpdateView):
    model = Trip
    form_class = DateForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class TripDelete(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = '/trips/'

@login_required
def add_transportation(request, trip_id):
    form = TransportationForm(request.POST)
    if form.is_valid():
        new_transportation_stretch = form.save(commit=False)
        new_transportation_stretch.trip_id = trip_id
        new_transportation_stretch.save()
    return redirect('trip-detail', trip_id=trip_id)

class TransportationCreate(LoginRequiredMixin, CreateView):
    model = Transportation_stretch
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TransportationUpdate(LoginRequiredMixin, UpdateView):
    model = Transportation_stretch
    fields = '__all__'
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TransportationDelete(LoginRequiredMixin, DeleteView):
    model = Transportation_stretch
