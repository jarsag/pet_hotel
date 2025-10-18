from django.db import models

class Owner(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"

class Pet(models.Model):
    PET_TYPES = (('dog', 'Собака'), ('cat', 'Кошка'), ('other', 'Другое'))
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=PET_TYPES)
    breed = models.CharField(max_length=100, blank=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    special_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"

class Room(models.Model):
    room_number = models.CharField(max_length=10, unique=True)
    type = models.CharField(max_length=100)  # "Стандарт", "Люкс"
    price_per_day = models.DecimalField(max_digits=8, decimal_places=2)
    
    def __str__(self):
        return f"Комната {self.room_number}"

class Booking(models.Model):
    STATUSES = (('booked', 'Забронирован'), ('active', 'Проживает'), ('completed', 'Завершено'))
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUSES, default='booked')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
   
    def save(self, *args, **kwargs):
        # Расчет стоимости при сохранении
        if self.check_in_date and self.check_out_date:
            days = (self.check_out_date - self.check_in_date).days
            if days > 0:
                # Используем цену номера или 300 по умолчанию
                price_per_day = self.room.price_per_day if self.room.price_per_day else 300
                self.total_cost = days * price_per_day
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Бронирование {self.pet.name} - {self.room.room_number}"