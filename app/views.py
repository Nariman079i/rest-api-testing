#from django.shortcuts import render
from .serializer import *
from .models import *
from rest_framework.generics import *
# Create your views here.


class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDataApiView(ListAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer


class LocateApiView(ListAPIView):
    queryset = Locate.objects.all()
    serializer_class = LocateSerializer


class IndustrialApiView(ListAPIView):
    queryset = Industrial.objects.all()
    serializer_class = IndustrialSerializer

