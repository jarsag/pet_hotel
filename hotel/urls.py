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
    path('owner/<int:pk>/', views.owner_detail, name='owner_detail'),
    path('pet/<int:pk>/', views.pet_detail, name='pet_detail'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('booking/<int:pk>/', views.booking_detail, name='booking_detail'),
    path('pet/new/owner/<int:owner_id>/', views.pet_create_for_owner, name='pet_create_for_owner'),
    path('room/range/', views.room_create_range, name='room_create_range'),
]