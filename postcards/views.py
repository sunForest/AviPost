from django.shortcuts import render
from rest_framework import viewsets
from .models import Postcard

class PostcardViewSet(viewsets.ModelViewSet):
    queryset = Postcard.objects.all()

# Create your views here.
