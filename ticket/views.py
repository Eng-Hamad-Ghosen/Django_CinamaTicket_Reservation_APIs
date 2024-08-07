from django.shortcuts import render
from django.http.response import JsonResponse
from.models import Guest,Movie,Reservation
from .serializers import GuestSerializer,MovieSerializer,ReservationSerializer


from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics,mixins,viewsets
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


#3.2 [GET,PUT,DELETE]
@api_view(['GET','DELETE','PUT'])
def FBV_pk(request,pk):
    try:
        guest=Guest.objects.get(pk=pk)
    except Guest.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        serializer=GuestSerializer(guest)
        return Response(serializer.data,status=status.HTTP_302_FOUND)
    
    elif request.method=='PUT':
        serializer=GuestSerializer(guest,data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status= status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='DELETE':
        guest.delete()
        return Response (serializer.data,status=status.HTTP_204_NO_CONTENT)

#4 CBV
#4.1 [GET,POST]
class CBV_list(APIView):
    def get(self,request):  
        try:
            guest = Guest.objects.all()
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=GuestSerializer(guest,many=True)
        return Response(data=serializer.data ,status=status.HTTP_302_FOUND)
        
    def post(self,request):
        serializer=GuestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#4.2 CBV with pk [GET,PUT,DELETE]
class CBV_pk(APIView):
    def get(self,request,pk):
        try:
            guest= Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer=GuestSerializer(guest)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    
    def put(self,request,pk):
        try:
            guest= Guest.objects.get(pk=pk)
        except Guest.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer=GuestSerializer(guest,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        guest=Guest.objects.get(pk=pk)
        guest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        
#5 Mixins
#5.1 [GET , POST]
class Mixins_list(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    def get(self,request):
        return self.list(request)
    
    def post(self ,request):
        return self.create(request)
    
#5.2 [GET , PUT , DELETE] With pk
class Mixin_pk(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    
    def get(self,request,pk):
        return self.retrieve(request)
    
    def put(self,request,pk):
        return self.update(request)
    
    def delete(self,request,pk):
        return self.destroy(request)
    
#6 Generics
#6.1 [GET , POST]
class Generics_list(generics.ListCreateAPIView):
    queryset=Guest.objects.all()
    serializer_class=GuestSerializer
    
#6.2 [GET , PUT , DELETE] With pk
class Generics_pk(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guest.objects.all()
    serializer_class=GuestSerializer
    
#Viewsets [GET,POST, PUT , DELETE] With pk and Without
class Viewsets_guest(viewsets.ModelViewSet):
    queryset = Guest.objects.all()
    serializer_class=GuestSerializer
    