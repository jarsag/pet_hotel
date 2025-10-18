from django.contrib import admin
from .models import Owner, Pet, Room, Booking

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'first_name', 'phone']

@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'breed', 'owner']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'type', 'price_per_day']

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['pet', 'room', 'check_in_date', 'status']