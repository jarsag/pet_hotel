from django.urls import path
from . import views

urlpatterns = [
 path('', views.index, name='index'),
    path('owners/', views.owner_list, name='owner_list'),
    path('pets/', views.pet_list, name='pet_list'),
    path('rooms/', views.room_list, name='room_list'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('owner/<int:pk>/edit/', views.owner_edit, name='owner_edit'),
    path('pet/<int:pk>/edit/', views.pet_edit, name='pet_edit'),
    path('room/<int:pk>/edit/', views.room_edit, name='room_edit'),
    path('booking/<int:pk>/edit/', views.booking_edit, name='booking_edit'),
    path('owner/new/', views.owner_create, name='owner_create'),
    path('pet/new/', views.pet_create, name='pet_create'),
    path('room/new/', views.room_create, name='room_create'),
    path('booking/new/', views.booking_create, name='booking_create'),
    path('owner/<int:pk>/delete/', views.owner_delete, name='owner_delete'),
    path('pet/<int:pk>/delete/', views.pet_delete, name='pet_delete'),
    path('room/<int:pk>/delete/', views.room_delete, name='room_delete'),
    path('booking/<int:pk>/delete/', views.booking_delete, name='booking_delete'),
]