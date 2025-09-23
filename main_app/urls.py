from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('accounts/signup/', views.signup, name='signup'),

    path('trips/', views.trip_index, name='trip-index'),
    path('trips/create/', views.TripCreate.as_view(), name='trip-create'),
    path('trips/<int:trip_id>/', views.trip_detail, name='trip-detail'),
    path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trip-update'),
    path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trip-delete'),
    path('trips/<int:trip_id>/add-transportation', views.add_transportation, name='add-transportation'),
    path('trips/<int:trip_id>/associate-attraction/<int:attraction_id>/', views.associate_attraction, name='associate-attraction'),
    path('trips/<int:trip_id>/remove-attraction/<int:attraction_id>/', views.remove_attraction, name='remove-attraction'),

    path('transportation/create', views.TransportationCreate.as_view(), name='transportation-create'),
    path('transportation/<int:pk>/update', views.TransportationUpdate.as_view(), name='transportation-update'),
    path('transportation/<int:pk>/delete', views.TransportationDelete.as_view(), name='transportation-delete'),
    
    path('attractions/create', views.AttractionCreate.as_view(), name='attraction-create'),
    path('attractions/<int:pk>/', views.AttractionDetail.as_view(), name='attraction-detail'),
    path('attractions/', views.AttractionList.as_view(), name='attraction-index'),
    path('attractions/<int:pk>/update/', views.AttractionUpdate.as_view(), name='attraction-update'),    
    path('attractions/<int:pk>/delete/', views.AttractionDelete.as_view(), name='attraction-delete'),
    
    ]