from django import forms
from .models import Owner, Pet, Room, Booking

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = '__all__'

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = '__all__'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'