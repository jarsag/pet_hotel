from django.shortcuts import render, get_object_or_404, redirect
from .models import Owner, Pet, Room, Booking
from .forms import OwnerForm, PetForm, RoomForm, BookingForm

def index(request):
    return render(request, 'hotel/index.html')

def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'hotel/owner_list.html', {'owners': owners})

def pet_list(request):
    pets = Pet.objects.all()
    return render(request, 'hotel/pet_list.html', {'pets': pets})

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/room_list.html', {'rooms': rooms})

def booking_list(request):
    bookings = Booking.objects.all()
    return render(request, 'hotel/booking_list.html', {'bookings': bookings})

def owner_edit(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == "POST":
        form = OwnerForm(request.POST, instance=owner)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm(instance=owner)
    return render(request, 'hotel/owner_edit.html', {'form': form})

def pet_edit(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == "POST":
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm(instance=pet)
    return render(request, 'hotel/pet_edit.html', {'form': form})

def room_edit(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'hotel/room_edit.html', {'form': form})

def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'hotel/booking_edit.html', {'form': form})

def owner_create(request):
    if request.method == "POST":
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('owner_list')
    else:
        form = OwnerForm()
    return render(request, 'hotel/owner_edit.html', {'form': form})

def pet_create(request):
    if request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pet_list')
    else:
        form = PetForm()
    return render(request, 'hotel/pet_edit.html', {'form': form})

def room_create(request):
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'hotel/room_edit.html', {'form': form})

def booking_create(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_list')
    else:
        form = BookingForm()
    return render(request, 'hotel/booking_edit.html', {'form': form})

def owner_delete(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    if request.method == "POST":
        owner.delete()
        return redirect('owner_list')
    return render(request, 'hotel/owner_delete.html', {'owner': owner})

def pet_delete(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    if request.method == "POST":
        pet.delete()
        return redirect('pet_list')
    return render(request, 'hotel/pet_delete.html', {'pet': pet})

def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        room.delete()
        return redirect('room_list')
    return render(request, 'hotel/room_delete.html', {'room': room})

def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.method == "POST":
        booking.delete()
        return redirect('booking_list')
    return render(request, 'hotel/booking_delete.html', {'booking': booking})

def owner_detail(request, pk):
    owner = get_object_or_404(Owner, pk=pk)
    return render(request, 'hotel/owner_detail.html', {'owner': owner})

def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, 'hotel/pet_detail.html', {'pet': pet})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'hotel/room_detail.html', {'room': room})

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'hotel/booking_detail.html', {'booking': booking})