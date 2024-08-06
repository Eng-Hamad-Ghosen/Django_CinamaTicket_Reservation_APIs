from django.shortcuts import render
from django.http.response import JsonResponse
from.models import Guest,Movie,Reservation
from .serializers import GuestSerializer,MovieSerializer,ReservationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

#1 without Resetframework and no model query
def no_rest_no_model(request):
    guest={
        'id':1,
        'name':'Hamad',
        'mobile':123456789
        
    }
    return JsonResponse(guest,safe=False)

#2 no_RestFramework and with Model
def no_rest_with_model(request):
    data=Guest.objects.all()
    # datta_moive=Movie.objects.all()
    # datta_reservation=Reservation.objects.all()
    response = {
        
        'guest':list(data.values_list('name','mobile'))
    }
    return JsonResponse(response)

#3 FBV
#3.1 [GET,POST]
@api_view(['GET','POST'])
def FBV_list(request):
    #GET
    if request.method=='GET':
        try:
            guest=Guest.objects.all()
            
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=GuestSerializer(guest,many=True)
        return Response(serializer.data)
    
    #POST
    elif request.method=='POST':
        serializer=GuestSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


#3.2 [PUT,DELETE]
# @api_view(['PUT','DELETE'])
# def rest_model(request):
#     #PUT
#     if request.method=='PUT':
#         pass
#     #DELETE
#     if request.method=='DELETE':
#         pass