from django.db import models

class Owner(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

class Pet(models.Model):
    PET_TYPES = (('dog', 'Собака'), ('cat', 'Кошка'), ('other', 'Другое'))
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=PET_TYPES)
    breed = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    special_notes = models.TextField(blank=True)

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=100)  # "Стандарт", "Люкс"
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)

class Booking(models.Model):
    STATUSES = (('booked', 'Забронирован'), ('active', 'Проживает'), ('completed', 'Завершено'))
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUSES, default='booked')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)