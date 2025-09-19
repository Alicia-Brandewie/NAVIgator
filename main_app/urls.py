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
    # path('trips/<int:trip_id>/add-transportation', views.add_transportation, name='add-transportation'),

    # path('transportation/create', views.TransportationCreate.as_view(), name='transportation-create'),
    # path('transportation/<int:pk>/update', views.TransportationUpdate.as_view(), name='transportation-update'),
    # path('transportation/<int:pk>/delete', views.TransportationUpdate.as_view(), name='transportation-delete'),
    ]