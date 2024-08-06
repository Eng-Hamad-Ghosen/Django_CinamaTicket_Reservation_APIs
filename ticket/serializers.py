from rest_framework import serializers
from .models import Guest,Movie,Reservation

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
                
class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
                
class GuestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Guest
<<<<<<< HEAD
        fields=['pk','reservation_guest','name','mobile']
=======
        fields=['pk','reservation_guste','name','mobile']
>>>>>>> ab26fb22a302a125c3ce5e6ec486d9bb72884fd8
