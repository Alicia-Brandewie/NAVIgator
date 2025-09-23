from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Trip, Attraction, Transportation
from .forms import DateForm, TransportationForm
from django.db import models
from django.views.generic import ListView, DetailView
from django.urls import reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


#__________Public Views__________#
class Home(LoginView):
    template_name = 'home.html'

def about(request):
    return render(request, 'about.html')

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

#__________Athorized-only Views__________#
@login_required
def trip_index(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'trips/index.html', {'trips': trips})

@login_required
def trip_detail(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    transportation_form = TransportationForm()
    attractions_trip_doesnt_have = Attraction.objects.exclude(id__in = trip.attractions.all().values_list('id'))
    return render(request, 'trips/detail.html', {
        'trip': trip,
        'transportation_form': transportation_form,
        'attractions': attractions_trip_doesnt_have
    })

class TripCreate(LoginRequiredMixin, CreateView):
        model = Trip
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
        transportation = form.save(commit=False)
        transportation.trip_id = trip_id
        transportation.save()
    return redirect('trip-detail', trip_id=trip_id)

class TransportationCreate(LoginRequiredMixin, CreateView):
    model = Transportation
    fields = "__all__"
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TransportationUpdate(LoginRequiredMixin, UpdateView):
    model = Transportation
    fields = ['type', 'company', 'departure_location', 'destination_location','ticket_number','notes']
    def get_success_url(self):
        trip_pk = self.object.trip.pk
        return reverse('trip-detail', kwargs={'trip_id':trip_pk})

class TransportationDelete(LoginRequiredMixin, DeleteView):
    model = Transportation
    def get_success_url(self):
        trip_pk = self.object.trip.pk
        return reverse('trip-detail', kwargs={'trip_id':trip_pk})

class AttractionCreate(LoginRequiredMixin, CreateView):
    model = Attraction
    fields = '__all__'

class AttractionList(LoginRequiredMixin, ListView):
    model = Attraction

class AttractionDetail(LoginRequiredMixin, DetailView):
    model = Attraction

class AttractionUpdate(LoginRequiredMixin, UpdateView):
    model = Attraction
    fields = '__all__'

class AttractionDelete(LoginRequiredMixin, DeleteView):
    model = Attraction
    success_url = '/attractions/'

@login_required
def associate_attraction(request, trip_id, attraction_id):
    Trip.objects.get(id=trip_id).attractions.add(attraction_id)
    return redirect('trip-detail', trip_id=trip_id)

@login_required
def remove_attraction(request, trip_id, attraction_id):
    trip = Trip.objects.get(id=trip_id)
    attraction = Attraction.objects.get(id=attraction_id)
    trip.attractions.remove(attraction)
    return redirect('trip-detail', trip_id=trip.id)