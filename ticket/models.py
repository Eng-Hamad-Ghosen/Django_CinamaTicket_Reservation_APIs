from django.db import models
from django.contrib.auth.models import User

#For def auto_generate_token
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
# Create your models here.

#Guset=customer ,Movie=Hall , Reservation


class Movie(models.Model):
    hall=models.CharField(max_length=50)#رقم الصالة ا, القاعة
    movie=models.CharField(max_length=50)
    # date=models.DateField()
    def __str__(self):
        return self.movie
    
    
class Guest(models.Model):
    name=models.CharField( max_length=50)
    mobile=models.IntegerField()
    
    def __str__(self) -> str:
        return self.name
    
    
    
class Reservation(models.Model):
    guest=models.ForeignKey("Guest",related_name='reservation_guest',on_delete=models.CASCADE)
    movie=models.ForeignKey("Movie",related_name='reservation_movie',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.guest.name +' -&- '+ self.movie.movie
    
    
class Post(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    body=models.TextField()
    
    
@receiver(post_save , sender=settings.AUTH_USER_MODEL)
def auto_generate_token(sender , instance , created , **kwargs):
    if created:
        Token.objects.create(user = instance)