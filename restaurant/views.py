from django.shortcuts import render

# Create your views here.
from .serializers import MenuSerializer,BookingSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Booking,Menu
from rest_framework.viewsets import ModelViewSet
# Create your views here.

class MenuView(APIView):
    def get(self,request):
        
     items=Menu.objects.all()
     
     serializer=MenuSerializer(items,many=True)
     return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
class BookingView(APIView):
    
    def get(self,request):
        
     items=Booking.objects.all()
     
     serializer=BookingSerializer(items,many=True)
     return Response(serializer.data)
    
    def post(self,request):
        serializer=BookingSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
                
                

class BookingViewSet(ModelViewSet):
    bookings=Booking.objects.all()
    serializer_class=BookingSerializer(bookings,many=True)
                    