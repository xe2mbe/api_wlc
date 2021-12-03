from django.shortcuts import render

# Create your views here.
from .models import guestUser
from .serializers import guestUserSerializer
from rest_framework import viewsets

class guestUserViewSet(viewsets.ModelViewSet):
  queryset = guestUser.objects.all()
  serializer_class = guestUserSerializer